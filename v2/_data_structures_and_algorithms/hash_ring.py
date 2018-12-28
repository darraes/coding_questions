from random import randint
from bisect import bisect_left, bisect_right
from collections import namedtuple

Range = namedtuple("Range", ["start", "count"])


class Node(object):
    def __init__(self, start, data=None):
        self.start = start
        self.data = data

    def __lt__(self, other):
        return self.start < other.start

    def __eq__(self, other):
        return self.start == other.start and self.data == other.data


class MoveRequest(object):
    def __init__(self, from_node, to_node, ranges):
        self.from_node = from_node
        self.to_node = to_node
        self.ranges = ranges

    def __str__(self):
        return "{} -> {} [{}]".format(
            self.from_node.data,
            self.to_node.data,
            ", ".join([str(r) for r in self.ranges]),
        )

    def __eq__(self, other):
        return (
            self.from_node == other.from_node
            and self.to_node == other.to_node
            and self.ranges == other.ranges
        )


class HashRing(object):
    RING_SIZE = 1000000000  # 1 Billion

    def __init__(self, spreading_factor=1):
        self.spreading_factor = spreading_factor
        self.ring = []

    def add(self, data, generator=lambda: randint(0, HashRing.RING_SIZE - 1)):
        '''
        Adds @self.spreading_factor new nodes to the ring. All new nodes will point
        to @data.

        :data: str         The data handing on the nodes being added. E.g. Shard name
        :generator: int()  The function to generate the new nodes ring locations
                           Must return a number in interval [0 - 1B)
        '''
        new_nodes = []
        moves = []
        for _ in range(self.spreading_factor):
            # TODO: The generator can create a node with the same hash.
            # If that happens, we should generate a new hash
            node = Node(start=generator(), data=data)
            new_nodes.append(node)

            if len(self.ring) == 0:
                continue

            from_node_idx = self._find_partition_idx(node.start)

            if from_node_idx > 0 and from_node_idx < len(self.ring):
                # Default case. The new node will be in between 2 nodes.
                moves.append(
                    MoveRequest(
                        from_node=self.ring[from_node_idx - 1],
                        to_node=node,
                        ranges=[
                            Range(
                                node.start, self.ring[from_node_idx].start - node.start
                            )
                        ],
                    )
                )
            elif from_node_idx == 0:
                # New node must be the new index 0. It's hash is smaller than the hash
                # of the current node at index 0
                moves.append(
                    MoveRequest(
                        from_node=self.ring[-1],
                        to_node=node,
                        ranges=[
                            Range(
                                node.start, self.ring[from_node_idx].start - node.start
                            )
                        ],
                    )
                )
            else:
                # from_node_idx == len(self.ring)
                # The new node will be the new last node
                moves.append(
                    MoveRequest(
                        from_node=self.ring[from_node_idx - 1],
                        to_node=node,
                        ranges=[
                            Range(0, self.ring[0].start),
                            Range(node.start, HashRing.RING_SIZE - node.start),
                        ],
                    )
                )

        self.ring.extend(new_nodes)
        self.ring.sort()

        return self._collapse_intersecting_moves(moves)

    def _collapse_intersecting_moves(self, moves):
        # TODO
        return moves

    def find(self, partition_key):
        partition_hash = hash(partition_key) % HashRing.RING_SIZE
        return self._find_partition(partition_hash)

    def _find_partition(self, partition_hash):
        node_idx = self._find_partition_idx(partition_hash)
        # If node_idx is 0, that means the current hash is smaller than the hash of the
        # node at index 0 therefore we need to grab the last node of the ring
        # (cicle to the back)
        return self.ring[node_idx - 1] if node_idx > 0 else self.ring[-1]

    def _find_partition_idx(self, partition_hash):
        return bisect_right(self.ring, Node(partition_hash))

    def print_ring(self):
        print(" | ".join(["{} ({})".format(n.data, n.start) for n in self.ring]))


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_insert_on_middle(self):
        vertexes = [200000000, 500000000, 800000000]
        idx = -1

        def generator():
            nonlocal vertexes, idx
            idx += 1
            return vertexes[idx]

        ring = HashRing(spreading_factor=3)
        ring.add("shard_0", generator=generator)
        ring.spreading_factor = 1

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_0", ring._find_partition(300000000).data)
        self.assertEqual("shard_0", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_0", ring._find_partition(600000000).data)
        self.assertEqual("shard_0", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)

        moves = ring.add("shard_1", generator=lambda: 300000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(200000000, "shard_0"),
                    Node(300000000, "shard_1"),
                    [Range(300000000, 500000000 - 300000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_1", ring._find_partition(300000000).data)
        self.assertEqual("shard_1", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_0", ring._find_partition(600000000).data)
        self.assertEqual("shard_0", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)

        moves = ring.add("shard_1", generator=lambda: 600000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(500000000, "shard_0"),
                    Node(600000000, "shard_1"),
                    [Range(600000000, 800000000 - 600000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_1", ring._find_partition(300000000).data)
        self.assertEqual("shard_1", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_1", ring._find_partition(600000000).data)
        self.assertEqual("shard_1", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)

    def test_insert_new_last(self):
        ring = HashRing()
        ring.add("shard_0", generator=lambda: 200000000)

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_0", ring._find_partition(300000000).data)
        self.assertEqual("shard_0", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_0", ring._find_partition(600000000).data)
        self.assertEqual("shard_0", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)

        # Test for when the ring has a single node
        moves = ring.add("shard_1", generator=lambda: 400000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(200000000, "shard_0"),
                    Node(400000000, "shard_1"),
                    [Range(0, 200000000), Range(400000000, 1000000000 - 400000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_1", ring._find_partition(0).data)
        self.assertEqual("shard_1", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_0", ring._find_partition(300000000).data)
        self.assertEqual("shard_1", ring._find_partition(400000000).data)
        self.assertEqual("shard_1", ring._find_partition(500000000).data)
        self.assertEqual("shard_1", ring._find_partition(600000000).data)
        self.assertEqual("shard_1", ring._find_partition(700000000).data)
        self.assertEqual("shard_1", ring._find_partition(800000000).data)
        self.assertEqual("shard_1", ring._find_partition(900000000).data)

        # Test for when the ring has multiple node
        moves = ring.add("shard_2", generator=lambda: 600000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(400000000, "shard_1"),
                    Node(600000000, "shard_2"),
                    [Range(0, 200000000), Range(600000000, 1000000000 - 600000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_2", ring._find_partition(0).data)
        self.assertEqual("shard_2", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_0", ring._find_partition(300000000).data)
        self.assertEqual("shard_1", ring._find_partition(400000000).data)
        self.assertEqual("shard_1", ring._find_partition(500000000).data)
        self.assertEqual("shard_2", ring._find_partition(600000000).data)
        self.assertEqual("shard_2", ring._find_partition(700000000).data)
        self.assertEqual("shard_2", ring._find_partition(800000000).data)
        self.assertEqual("shard_2", ring._find_partition(900000000).data)

    def test_insert_on_idx_zero(self):
        ring = HashRing()
        ring.add("shard_0", generator=lambda: 500000000)

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_0", ring._find_partition(300000000).data)
        self.assertEqual("shard_0", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_0", ring._find_partition(600000000).data)
        self.assertEqual("shard_0", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)

        # Test for when the ring has a single node
        moves = ring.add("shard_1", generator=lambda: 200000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(500000000, "shard_0"),
                    Node(200000000, "shard_1"),
                    [Range(200000000, 500000000 - 200000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(100000000).data)
        self.assertEqual("shard_1", ring._find_partition(200000000).data)
        self.assertEqual("shard_1", ring._find_partition(300000000).data)
        self.assertEqual("shard_1", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_0", ring._find_partition(600000000).data)
        self.assertEqual("shard_0", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)

        # Test for when the ring has multiple nodes
        moves = ring.add("shard_2", generator=lambda: 100000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(500000000, "shard_0"),
                    Node(100000000, "shard_2"),
                    [Range(100000000, 200000000 - 100000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_2", ring._find_partition(100000000).data)
        self.assertEqual("shard_1", ring._find_partition(200000000).data)
        self.assertEqual("shard_1", ring._find_partition(300000000).data)
        self.assertEqual("shard_1", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_0", ring._find_partition(600000000).data)
        self.assertEqual("shard_0", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)


if __name__ == "__main__":
    unittest.main()