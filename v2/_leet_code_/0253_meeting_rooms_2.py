import heapq
from typing import List

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []

        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()

        s_idx = e_idx = max_rooms = 0
        while s_idx < len(starts):
            if ends[e_idx] <= starts[s_idx]:
                max_rooms -= 1
                e_idx += 1

            max_rooms += 1
            s_idx += 1

        return max_rooms

    def minMeetingRooms2(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        heap = []

        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
        return len(heap)


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            2, s.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)])
        )
        self.assertEqual(1, s.minMeetingRooms([Interval(7, 10), Interval(2, 4)]))
        self.assertEqual(1, s.minMeetingRooms([Interval(0, 30)]))
        self.assertEqual(0, s.minMeetingRooms([]))


if __name__ == "__main__":
    unittest.main()
