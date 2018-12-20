class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __str__(self):
        return "[{}, {}]".format(self.lower, self.upper)

    def __eq__(self, that):
        return self.lower == that.lower and self.upper == that.upper


def merge_interval(arr, interval):
    ans = []
    i = 0

    while i < len(arr) and arr[i].upper < interval.lower:
        ans.append(arr[i])
        i += 1

    ans.append(interval)

    while i < len(arr):
        last = ans[-1]
        if arr[i].lower < last.upper:
            last.lower = min(last.lower, arr[i].lower)
            last.upper = max(last.upper, arr[i].upper)
        else:
            ans.append(arr[i])
        i += 1

    return ans


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
        self.assertEqual(
            [Interval(1, 5), Interval(10, 27)],
            merge_interval(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(12, 27)
            ),
        )

        self.assertEqual(
            [Interval(1, 5), Interval(10, 15), Interval(20, 25)],
            merge_interval(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(11, 13)
            ),
        )

        self.assertEqual(
            [Interval(1, 15), Interval(20, 25)],
            merge_interval(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(4, 13)
            ),
        )

        self.assertEqual(
            [Interval(1, 5), Interval(6, 9), Interval(10, 15), Interval(20, 25)],
            merge_interval(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(6, 9)
            ),
        )
        self.assertEqual(
            [Interval(1, 5), Interval(10, 15), Interval(20, 25), Interval(60, 99)],
            merge_interval(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(60, 99)
            ),
        )

        self.assertEqual(
            [Interval(-1, 0), Interval(1, 5), Interval(10, 15), Interval(20, 25)],
            merge_interval(
                [Interval(1, 5), Interval(10, 15), Interval(20, 25)], Interval(-1, 0)
            ),
        )


if __name__ == "__main__":
    unittest.main()
