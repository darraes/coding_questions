class Solution:
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def _rob(nums, i, lookup):
            if i < 0:
                return 0

            if i in lookup:
                return lookup[i]

            lookup[i] = max(
                nums[i] + _rob(nums, i - 2, lookup), _rob(nums, i - 1, lookup)
            )
            return lookup[i]
        return _rob(nums, len(nums) - 1, {})

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
            
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]

        for i in range(2, len(memo)):
            memo[i] = max(nums[i - 1] + memo[i - 2], memo[i - 1])

        return memo[-1]


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(4, s.rob([1,2,3,1]))
        self.assertEqual(12, s.rob([2,7,9,3,1]))
        self.assertEqual(0, s.rob([]))
        self.assertEqual(1, s.rob([1]))
        self.assertEqual(2, s.rob([2,1]))
        self.assertEqual(4, s.rob([2,1,1,2]))


if __name__ == '__main__':
    unittest.main()