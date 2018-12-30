class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):
                bump = 0
                if nums[j] < nums[i]:
                    bump = 1
                lookup[i] = max(lookup[i], bump + nums[j])
        return lookup[-1]



###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(4, s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))


if __name__ == "__main__":
    unittest.main()
