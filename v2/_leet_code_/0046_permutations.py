class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self._permute(nums, 0)

    def _permute(self, nums, i):
        if i == len(nums):
            return [[]]

        current = nums[i]
        results = []

        sub_perms = self._permute(nums, i + 1)
        for perm in sub_perms:
            for j in range(len(perm) + 1):
                results.append(perm[:j] + [current] + perm[j:])
        return results


###############################################################
import unittest
import sys


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]],
            s.permute([1, 2, 3]),
        )


if __name__ == "__main__":
    unittest.main()
