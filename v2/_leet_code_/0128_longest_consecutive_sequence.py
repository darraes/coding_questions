class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest_streak = 0
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
        self.assertEqual(1, s.longestConsecutive([100, 4, 200]))
        self.assertEqual(8, s.longestConsecutive([100, 4, 200, 1, 3, 2, 5, 7, 6, 8]))
        self.assertEqual(0, s.longestConsecutive([]))


if __name__ == "__main__":
    unittest.main()
