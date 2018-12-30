class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        lookup = [1] * len(nums)
        gmax = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    lookup[i] = max(lookup[i], 1 + lookup[j])
            gmax = max(gmax, lookup[i])

        return gmax



###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLIS([4,10,4,3,8,9]))
        self.assertEqual(4, s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(5, s.lengthOfLIS([1, 2, 3, 4, 5]))
        self.assertEqual(1, s.lengthOfLIS([10, 9, 8, 7, 6]))
        self.assertEqual(1, s.lengthOfLIS([10, 9]))
        self.assertEqual(1, s.lengthOfLIS([10]))
        self.assertEqual(0, s.lengthOfLIS([]))


if __name__ == "__main__":
    unittest.main()
