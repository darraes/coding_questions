class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest_streak = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                current_streak = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(4, s.longestConsecutive([100, 4, 200, 1, 3, 2]))


if __name__ == "__main__":
    unittest.main()