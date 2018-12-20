class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self._permute(nums, 0)

    def _permute(self, nums, i):
        if i == len(nums):
            return [[]]

        current = nums[i]
        results = []

        sub_perms = self._permute(nums, i + 1)
        for perm in sub_perms:
            for j in range(len(perm) + 1):
                if j == 0 or current != perm[j - 1]:
                    results.append(perm[:j] + [current] + perm[j:])
                else:
                    break
        return results


###############################################################
import unittest
import sys


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([[1, 1, 2], [1, 2, 1], [2, 1, 1]], s.permuteUnique([1, 2, 1]))
        self.assertEqual(
            [[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [2, 1, 1, 1]],
            s.permuteUnique([1, 2, 1, 1]),
        )


if __name__ == "__main__":
    unittest.main()
