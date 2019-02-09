from heapq import heappush, heappop
from collections import namedtuple

Point = namedtuple("Point", ["negH", "pos"])


class Solution:
    def getSkyline(self, buildings: "List[List[int]]") -> "List[List[int]]":
        critical_points = [(L, -H, R) for L, R, H in buildings]
        critical_points += [(R, 0, 0) for _, R, _ in buildings]
        critical_points.sort()

        key_points = []
        heap = []
        for pos, negH, R in critical_points:
            # heapq doesn't have a remove to be used on right points.
            # Remove all past points sitting on top
            while heap and heap[0].pos <= pos:
                heappop(heap)
            # If is left point it is the start of a building. Add to heap
            if negH != 0:
                heappush(heap, Point(negH, R))
            # If the top of the heap is not already added, do it
            highest = -heap[0].negH if heap else 0
            if not key_points or key_points[-1][1] != highest:
                key_points.append([pos, highest])
        return key_points


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
            s.getSkyline(
                [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
            ),
        )


if __name__ == "__main__":
    unittest.main(exit=False)
