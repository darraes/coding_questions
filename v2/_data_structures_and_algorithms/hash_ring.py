from random import randint
from bisect import bisect_left, bisect_right
from collections import namedtuple

Range = namedtuple("Range", ["start", "end"])


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
                moves.append(
                    MoveRequest(
                        from_node=self.ring[from_node_idx - 1],
                        to_node=node,
                        ranges=[Range(node.start, self.ring[from_node_idx].start)],
                    )
                )
            elif from_node_idx == 0:
                moves.append(
                    MoveRequest(
                        from_node=self.ring[-1],
                        to_node=node,
                        ranges=[Range(node.start, self.ring[from_node_idx].start)],
                    )
                )
            else:  # from_node_idx == len(self.ring) {New last entry}
                 moves.append(
                    MoveRequest(
                        from_node=self.ring[from_node_idx],
                        to_node=node,
                        ranges=[
                            Range(0, node.start),
                            Range(self.ring[0].start, HashRing.RING_SIZE),
                        ],
                    )
                )

        self.ring.extend(new_nodes)
        self.ring.sort()
        return moves

    def find(self, partition_key):
        partition_hash = hash(partition_key) % HashRing.RING_SIZE
        return self._find_partition(partition_hash)

    def _find_partition(self, partition_hash):
        node_idx = self._find_partition_idx(partition_hash)
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
                    [Range(300000000, 500000000)],
                )
            ],
            moves,
        )

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
                    [Range(600000000, 800000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_0", ring._find_partition(100000000).data)
        self.assertEqual("shard_0", ring._find_partition(200000000).data)
        self.assertEqual("shard_1", ring._find_partition(300000000).data)
        self.assertEqual("shard_1", ring._find_partition(400000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_1", ring._find_partition(600000000).data)
        self.assertEqual("shard_1", ring._find_partition(700000000).data)
        self.assertEqual("shard_0", ring._find_partition(800000000).data)
        self.assertEqual("shard_0", ring._find_partition(900000000).data)



    def test_insert_on_idx_zero(self):
        ring = HashRing()
        ring.add("shard_0", generator=lambda: 500000000)

        # Test for when the ring has a single node
        moves = ring.add("shard_1", generator=lambda: 250000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(500000000, "shard_0"),
                    Node(250000000, "shard_1"),
                    [Range(250000000, 500000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_0", ring._find_partition(500000001).data)
        self.assertEqual("shard_0", ring._find_partition(999999999).data)
        self.assertEqual("shard_0", ring._find_partition(240000000).data)
        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(249999999).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)

        self.assertEqual("shard_1", ring._find_partition(250000000).data)
        self.assertEqual("shard_1", ring._find_partition(250000001).data)
        self.assertEqual("shard_1", ring._find_partition(350000000).data)
        self.assertEqual("shard_1", ring._find_partition(499999999).data)

        # Test for when the ring has multiple nodes
        moves = ring.add("shard_2", generator=lambda: 100000000)
        self.assertEqual(
            [
                MoveRequest(
                    Node(500000000, "shard_0"),
                    Node(100000000, "shard_2"),
                    [Range(100000000, 250000000)],
                )
            ],
            moves,
        )

        self.assertEqual("shard_2", ring._find_partition(100000000).data)
        self.assertEqual("shard_2", ring._find_partition(240000000).data)
        self.assertEqual("shard_2", ring._find_partition(249999999).data)

        self.assertEqual("shard_0", ring._find_partition(0).data)
        self.assertEqual("shard_0", ring._find_partition(99999999).data)
        self.assertEqual("shard_0", ring._find_partition(500000000).data)
        self.assertEqual("shard_0", ring._find_partition(500000001).data)
        self.assertEqual("shard_0", ring._find_partition(999999999).data)

        self.assertEqual("shard_1", ring._find_partition(250000000).data)
        self.assertEqual("shard_1", ring._find_partition(250000001).data)
        self.assertEqual("shard_1", ring._find_partition(350000000).data)
        self.assertEqual("shard_1", ring._find_partition(499999999).data)


if __name__ == "__main__":
    unittest.main()
