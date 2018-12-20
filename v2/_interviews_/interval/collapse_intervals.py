# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, that):
        return self.start == that.start and self.end == that.end


def collapse(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    ans = []
    current = None

    intervals.sort(key=lambda interval: interval.start)

    i = 0
    while i < len(intervals):
        if not current:
            current = intervals[i]
        else:
            if current.end >= intervals[i].start:
                current.end = max(current.end, intervals[i].end)
            else:
                ans.append(current)
                current = None
                i -= 1
        i += 1

    if current:
        ans.append(current)
    return ans


###############################################################
import unittest


def make(s, e):
    return Interval(s, e)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            [make(1, 6), make(8, 10), make(15, 18)],
            collapse([make(1, 3), make(2, 6), make(8, 10), make(15, 18)]),
        )
        self.assertEqual([make(1, 5)], collapse([make(1, 4), make(4, 5)]))
        self.assertEqual([make(1, 7)], collapse([make(1, 7), make(4, 5)]))
        self.assertEqual([make(1, 7)], collapse([make(1, 5), make(1, 7)]))

        self.assertEqual(
            [make(1, 3), make(5, 6), make(8, 10), make(15, 18)],
            collapse([make(1, 3), make(5, 6), make(8, 10), make(15, 18)]),
        )


if __name__ == "__main__":
    unittest.main()


UYHLDJ

QEVJUK
