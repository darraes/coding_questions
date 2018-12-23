class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self._findTargetSumWays(nums, S, 0, {})

    def _findTargetSumWays(self, nums, S, i, lookup):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if S == 0 and i == len(nums):
            return 1
        if i == len(nums):
            return 0

        if (S, i) in lookup:
            return lookup[(S, i)]

        count = 0
        count += self._findTargetSumWays(nums, S - nums[i], i + 1, lookup)
        count += self._findTargetSumWays(nums, S + nums[i], i + 1, lookup)

        lookup[(S, i)] = count
        return count



###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(5, s.findTargetSumWays([1, 1, 1, 1, 1], 3))
        self.assertEqual(2, s.findTargetSumWays([1, 7, 2, 1, -4], 5))


if __name__ == "__main__":
    unittest.main()