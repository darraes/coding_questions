class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = self._combine(candidates, target, 0, {})
        res.reverse()
        return res

    def _combine(self, candidates, target, level, cache):
        if target == 0:
            return [[]]
        if level == len(candidates):
            return []

        if (level, target) in cache:
            return cache[(level, target)]

        cur_sum = 0
        level_res = []
        usages = []
        while cur_sum <= target:
            sub_res = self._combine(candidates, target - cur_sum, level + 1, cache)

            for r in sub_res:
                level_res.append(usages + r)

            cur_sum += candidates[level]
            usages.append(candidates[level])

        cache[(level, target)] = level_res
        return level_res


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [[2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 8], [2, 4, 4], [5, 5]],
            s.combinationSum([2, 5, 8, 4], 10),
        )
        self.assertEqual([[2, 2, 3], [7]], s.combinationSum([2, 3, 6, 7], 7))
        self.assertEqual(
            [[2, 2, 2, 2], [2, 3, 3], [3, 5]], s.combinationSum([2, 3, 5], 8)
        )
        self.assertEqual([[2]], s.combinationSum([2, 3, 6, 7], 2))
        self.assertEqual([[2]], s.combinationSum([2], 2))
        self.assertEqual([], s.combinationSum([2], 3))
        self.assertEqual([], s.combinationSum([2, 4], 3))
        self.assertEqual([], s.combinationSum([], 3))
        self.assertEqual([[1, 1]], s.combinationSum([1], 2))
        self.assertEqual([[1, 1, 1, 1]], s.combinationSum([1], 4))


if __name__ == "__main__":
    unittest.main()
