from heapq import heappush, heappop
from collections import namedtuple, defaultdict

Cost = namedtuple("Cost", ["cost", "stops"])
Connection = namedtuple("Connection", ["dst", "price"])
Flight = namedtuple("Flight", ["acc_price", "stops", "local"])


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append(Connection(dst=flight[1], price=flight[2]))

        frontier = []
        heappush(frontier, Flight(acc_price=0, stops=-1, local=src))
        cost_so_far = {src: Cost(cost=0, stops=-1)}

        while len(frontier) > 0:
            current = heappop(frontier)

            if current.local == dst:
                return current.acc_price

            if current.stops < K:
                for connection in graph[current.local]:
                    cost_to_next = current.acc_price + connection.price
                    if (
                        connection.dst not in cost_so_far
                        or cost_to_next < cost_so_far[connection.dst].cost
                        or current.stops != cost_so_far[connection.dst].stops
                    ):
                        cost_so_far[connection.dst] = Cost(
                            cost=cost_to_next, stops=current.stops + 1
                        )
                        heappush(
                            frontier,
                            Flight(
                                acc_price=cost_to_next,
                                stops=current.stops + 1,
                                local=connection.dst,
                            ),
                        )
        return -1


###############################################################
import unittest


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
