import bisect


class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(0, s.search([1, 2, 3, 4], 1))
        self.assertEqual(3, s.search([5, 6, 7, 1, 2, 3, 4], 1))
        self.assertEqual(6, s.search([5, 6, 7, 1, 2, 3, 4], 4))
        self.assertEqual(0, s.search([5, 6, 7, 1, 2, 3, 4], 5))
        self.assertEqual(2, s.search([5, 6, 7, 1, 2, 3, 4], 7))
        self.assertEqual(-1, s.search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(-1, s.search([5, 6, 7, 0, 1, 2], 4))
        self.assertEqual(0, s.search([1], 1))
        self.assertEqual(-1, s.search([1], 2))
        self.assertEqual(0, s.search([2, 1], 2))
        self.assertEqual(1, s.search([1, 2], 2))
        self.assertEqual(1, s.search([3, 5, 1], 5))


if __name__ == "__main__":
    unittest.main()
