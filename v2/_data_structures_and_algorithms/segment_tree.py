from typing import List
import math


class SegmentTree:
    def __init__(self, arr: List[int], agg=lambda x, y: x + y):
        x = math.ceil(math.log(len(arr), 2))

        self.tree = [None] * (2 * (2 ** x - 1))
        self.len = len(arr)
        self.aggregator = agg

        self._build(arr)

    def _build(self, arr):
        def build_helper(idx: int, s: int, e: int):
            nonlocal arr
            if s == e:
                self.tree[idx] = arr[s]
                return arr[s]

            m = SegmentTree._mid(s, e)
            self.tree[idx] = self.aggregator(
                build_helper(2 * idx + 1, s, m), build_helper(2 * idx + 2, m + 1, e)
            )

            return self.tree[idx]

        build_helper(0, 0, self.len - 1)

    def segment(self, s: int, e: int):
        def segment_helper(idx: int, qs: int, qe: int, cs: int, ce: int):
            if cs >= qs and ce <= qe:
                return self.tree[idx]

            if ce < qs or cs > qe:
                return 0

            m = SegmentTree._mid(cs, ce)
            return self.aggregator(
                segment_helper(2 * idx + 1, qs, qe, cs, m),
                segment_helper(2 * idx + 2, qs, qe, m + 1, ce),
            )

        return segment_helper(0, s, e, 0, self.len - 1)

    def update(self, arr_i, diff):
        def update_helper(idx, diff, i, cs, ce):
            if i < cs or i > ce:
                return

            self.tree[idx] = self.aggregator(self.tree[idx], diff)
            if cs != ce:
                m = SegmentTree._mid(cs, ce)
                update_helper(2 * idx + 1, diff, i, cs, m)
                update_helper(2 * idx + 2, diff, i, m + 1, ce)

        if not (0 <= arr_i < self.len):
            raise "TODO Exception"

        update_helper(0, diff, arr_i, 0, self.len - 1)

    @staticmethod
    def _mid(s: int, e: int) -> int:
        return s + (e - s) // 2


#####################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_mergesort(self):
        stree = SegmentTree([1, 3, 5, 7, 9, 11])

        self.assertEqual(15, stree.segment(1, 3))
        self.assertEqual(24, stree.segment(1, 4))
        self.assertEqual(35, stree.segment(1, 5))
        self.assertEqual(12, stree.segment(2, 3))

        stree.update(arr_i=2, diff=+1)

        self.assertEqual(16, stree.segment(1, 3))
        self.assertEqual(25, stree.segment(1, 4))
        self.assertEqual(36, stree.segment(1, 5))
        self.assertEqual(13, stree.segment(2, 3))


if __name__ == "__main__":
    unittest.main(exit=False)
