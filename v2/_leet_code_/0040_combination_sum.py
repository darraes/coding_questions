import itertools


def sort_list(k):
    for l in k:
        l.sort()
    k.sort()
    return list(k for k, _ in itertools.groupby(k))


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = self._combine(candidates, target, 0, {})
        return sort_list(res)

    def _combine(self, candidates, target, level, cache):
        if target == 0:
            return [[]]
        if target < 0 or level == len(candidates):
            return []
        if (target, level) in cache:
            return cache[(target, level)]

        level_res = []
        sub_ans = self._combine(candidates, target, level + 1, cache)
        for tmp in sub_ans:
            level_res.append([] + tmp)

        if candidates[level] <= target:
            sub_ans = self._combine(
                candidates, target - candidates[level], level + 1, cache
            )
            for tmp in sub_ans:
                level_res.append(tmp + [candidates[level]])

        cache[(target, level)] = level_res
        return level_res


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            sort_list([[1, 2, 4], [2, 2, 3], [2, 5], [3, 4]]),
            s.combinationSum3([5, 3, 1, 2, 2, 4], 7),
        )
        self.assertEqual(
            sort_list([[1, 1, 2, 2], [1, 1, 4], [1, 2, 3], [2, 2, 2], [2, 4]]),
            s.combinationSum2([4, 4, 2, 1, 4, 2, 2, 1, 3], 6),
        )
        self.assertEqual(
            sort_list([[1, 2, 5], [1, 7], [1, 1, 6], [2, 6]]),
            s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8),
        )
        self.assertEqual(sort_list([[7]]), s.combinationSum2([2, 3, 6, 7], 7))
        self.assertEqual(sort_list([[2, 8]]), s.combinationSum2([2, 5, 8, 4], 10))
        self.assertEqual(
            sort_list([[3, 5], [2, 6]]), s.combinationSum2([2, 3, 5, 6], 8)
        )
        self.assertEqual(sort_list([[2]]), s.combinationSum2([2, 3, 6, 7], 2))
        self.assertEqual(
            sort_list([[3, 3], [2, 4]]), s.combinationSum2([2, 3, 3, 4, 7], 6)
        )
        self.assertEqual(
            sort_list([[2, 3], [2, 3]]), s.combinationSum2([2, 3, 3, 4, 7], 5)
        )
        self.assertEqual(sort_list([[2]]), s.combinationSum2([2], 2))
        self.assertEqual([], s.combinationSum2([2], 3))
        self.assertEqual([], s.combinationSum2([2, 4], 3))
        self.assertEqual([], s.combinationSum2([], 3))
        self.assertEqual([], s.combinationSum2([1], 2))


if __name__ == "__main__":
    unittest.main()
