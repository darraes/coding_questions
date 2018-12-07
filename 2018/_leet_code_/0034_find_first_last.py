from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)

        if r == 0 or nums[r - 1] != target:
            return [-1, -1]

        return [l, r - 1]


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([3, 4], s.searchRange([5, 7, 7, 8, 8, 10], 8))
        self.assertEqual([-1, -1], s.searchRange([5, 7, 7, 8, 8, 10], 6))
        self.assertEqual([0, 0], s.searchRange([5, 7, 7, 8, 8, 10], 5))
        self.assertEqual([5, 5], s.searchRange([5, 7, 7, 8, 8, 10], 10))
        self.assertEqual([-1, -1], s.searchRange([5, 7, 7, 8, 8, 10], 11))
        self.assertEqual([-1, -1], s.searchRange([5, 7, 7, 8, 8, 10], 3))

        self.assertEqual([-1, -1], s.searchRange([5], 8))
        self.assertEqual([-1, -1], s.searchRange([5], 6))
        self.assertEqual([0, 0], s.searchRange([5], 5))
        self.assertEqual([-1, -1], s.searchRange([5], 10))
        self.assertEqual([-1, -1], s.searchRange([5], 11))
        self.assertEqual([-1, -1], s.searchRange([5], 3))


if __name__ == "__main__":
    unittest.main()
