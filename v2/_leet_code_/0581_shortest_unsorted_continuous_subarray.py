class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = end = 0
        i = 1
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                start = i - 1
                break
            i += 1

        i = len(nums) - 1
        while i >= 0:
            if nums[i] < nums[i - 1]:
                end = i
                break
            i -= 1

        if start == end:
            return 0

        min_to_right = min(nums[start + 1 :])
        max_to_left = max(nums[:end])

        while start >= 0 and nums[start] > min_to_right:
            start -= 1

        while end < len(nums) and nums[end] < max_to_left:
            end += 1

        start += 1
        end -= 1

        return end - start + 1


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(5, s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
        self.assertEqual(5, s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15, 15]))
        self.assertEqual(6, s.findUnsortedSubarray([2, 6, 4, 8, 15, 10, 9, 15, 15]))
        self.assertEqual(5, s.findUnsortedSubarray([5, 4, 3, 2, 1]))
        self.assertEqual(0, s.findUnsortedSubarray([1, 2, 3]))
        self.assertEqual(0, s.findUnsortedSubarray([1, 2]))
        self.assertEqual(0, s.findUnsortedSubarray([1, 2, 2]))
        self.assertEqual(0, s.findUnsortedSubarray([1, 1, 2]))
        self.assertEqual(0, s.findUnsortedSubarray([2]))

        self.assertEqual(6, s.findUnsortedSubarray([2, 6, 4, 8, 16, 9, 15]))
        self.assertEqual(8, s.findUnsortedSubarray([2, 6, 4, 8, 1, 16, 9, 15]))


if __name__ == "__main__":
    unittest.main()
