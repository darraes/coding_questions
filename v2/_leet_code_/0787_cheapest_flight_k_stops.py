import unittest
from collections import defaultdict, namedtuple
from heapq import heappop, heappush
from typing import List

Cost = namedtuple("Cost", ["cost"])
Connection = namedtuple("Connection", ["dst", "price"])
Flight = namedtuple("Flight", ["acc_price", "stops", "local"])


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append(Connection(dst=flight[1], price=flight[2]))

        frontier = []
        heappush(frontier, Flight(acc_price=0, stops=-1, local=src))
        cost_so_far = {(src, -1): Cost(cost=0)}

        while len(frontier) > 0:
            current = heappop(frontier)

            if current.local == dst:
                return current.acc_price

            if current.stops < K:
                for connection in graph[current.local]:
                    cost_to_next = current.acc_price + connection.price
                    stops_to_next = current.stops + 1
                    if (
                        (connection.dst, stops_to_next) not in cost_so_far
                        or cost_to_next
                        < cost_so_far[(connection.dst, stops_to_next)].cost
                    ):
                        cost_so_far[connection.dst] = Cost(cost=cost_to_next)
                        heappush(
                            frontier,
                            Flight(
                                acc_price=cost_to_next,
                                stops=stops_to_next,
                                local=connection.dst,
                            ),
                        )
        return -1


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            7,
            s.findCheapestPrice(
                5,
                [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]],
                0,
                2,
                2,
            ),
        )

        self.assertEqual(
            200,
            s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
        )

        self.assertEqual(
            500,
            s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
        )

        self.assertEqual(-1, s.findCheapestPrice(3, [[0, 1, 100]], 0, 2, 0))

        self.assertEqual(-1, s.findCheapestPrice(3, [[0, 1, 100]], 2, 0, 0))


if __name__ == "__main__":
    unittest.main()
