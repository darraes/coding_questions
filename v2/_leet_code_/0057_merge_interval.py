# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[{},{}]".format(self.start, self.end)

    def __eq__(self, that):
        return self.start == that.start and self.end == that.end


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        new_intervals = []

        i = 0
        while i < len(intervals):
            if intervals[i].end >= newInterval.start:
                break
            new_intervals.append(intervals[i])
            i += 1

        new_intervals.append(newInterval)

        while i < len(intervals):
            if intervals[i].start <= new_intervals[-1].end:
                new_intervals[-1].end = max(new_intervals[-1].end, intervals[i].end)
                new_intervals[-1].start = min(
                    new_intervals[-1].start, intervals[i].start
                )
            else:
                new_intervals.append(intervals[i])
            i += 1

        return new_intervals


###############################################################
import unittest


def print_intervals(intervals):
    buffer = ""
    for interval in intervals:
        buffer += str(interval)
        buffer += " -> "
    print(buffer)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            [Interval(1, 5), Interval(6, 9)],
            s.insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5)),
        )

        self.assertEqual(
            [Interval(1, 2), Interval(3, 10), Interval(12, 16)],
            s.insert(
                [
                    Interval(1, 2),
                    Interval(3, 5),
                    Interval(6, 7),
                    Interval(8, 10),
                    Interval(12, 16),
                ],
                Interval(4, 8),
            ),
        )

        self.assertEqual(
            [Interval(1, 5), Interval(10, 27)],
            s.insert(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(12, 27)
            ),
        )

        self.assertEqual(
            [Interval(1, 5), Interval(10, 15), Interval(20, 25)],
            s.insert(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(11, 13)
            ),
        )

        self.assertEqual(
            [Interval(1, 15), Interval(20, 25)],
            s.insert(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(4, 13)
            ),
        )

        self.assertEqual(
            [Interval(1, 5), Interval(6, 9), Interval(10, 15), Interval(20, 25)],
            s.insert(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(6, 9)
            ),
        )
        self.assertEqual(
            [Interval(1, 5), Interval(10, 15), Interval(20, 25), Interval(60, 99)],
            s.insert(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(60, 99)
            ),
        )

        self.assertEqual(
            [Interval(-1, 0), Interval(1, 5), Interval(10, 15), Interval(20, 25)],
            s.insert(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(-1, 0)
            ),
        )


if __name__ == "__main__":
    unittest.main()
