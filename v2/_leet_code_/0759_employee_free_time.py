class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __str__(self):
        return "({},{})".format(self.start, self.end)


from heapq import heappush, heappop


class Solution:
    def employeeFreeTime(self, schedules):
        normalized_scheds = []
        for s in schedules:
            for interval in s:
                heappush(normalized_scheds, (interval.start, 1))
                heappush(normalized_scheds, (interval.end, -1))

        res = []
        pos, score = heappop(normalized_scheds)
        while normalized_scheds:
            n_pos, inc = heappop(normalized_scheds)

            if score == 0 and pos != n_pos:
                res.append(Interval(pos, n_pos))

            score += inc
            pos = n_pos
        return res


def print_ll(l):
    for i in l:
        print(i)


def to_interval_list(l):
    res = []
    for i in l:
        res.append(Interval(i[0], i[1]))
    return res


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            to_interval_list([[3, 4]]),
            s.employeeFreeTime(
                [
                    to_interval_list([[1, 2], [5, 6]]),
                    to_interval_list([[1, 3]]),
                    to_interval_list([[4, 10]]),
                ]
            ),
        )
        self.assertEqual(
            to_interval_list([[5, 6], [7, 9]]),
            s.employeeFreeTime(
                [
                    to_interval_list([[1, 3], [6, 7]]),
                    to_interval_list([[2, 4]]),
                    to_interval_list([[2, 5], [9, 12]]),
                ]
            ),
        )

        self.assertEqual(
            to_interval_list([]),
            s.employeeFreeTime(
                [to_interval_list([[1, 3], [6, 7]]), to_interval_list([[3, 6]])]
            ),
        )
        self.assertEqual(
            to_interval_list([]),
            s.employeeFreeTime(
                [to_interval_list([[2, 3], [6, 7]]), to_interval_list([[1, 8]])]
            ),
        )
        self.assertEqual(
            to_interval_list([]),
            s.employeeFreeTime(
                [to_interval_list([[1, 3], [3, 5]]), to_interval_list([[5, 8]])]
            ),
        )


if __name__ == "__main__":
    unittest.main()
