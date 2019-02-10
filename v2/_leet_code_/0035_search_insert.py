class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._search(nums, target, 0, len(nums) - 1)

    def _search(self, nums, target, s, e):
        while s <= e:
            # print(s, e)
            mid = int((s + e) / 2)

            if nums[mid] == target:
                return mid

            if s == e - 1 or s == e:
                if target <= nums[s]:
                    return s
                elif target > nums[e]:
                    return e + 1
                else:
                    return e

            if target < nums[mid]:
                e = mid
            else:
                s = mid


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(2, s.searchInsert([1, 3, 5, 6], 5))
        self.assertEqual(1, s.searchInsert([1, 3, 5, 6], 2))
        self.assertEqual(4, s.searchInsert([1, 3, 5, 6], 7))
        self.assertEqual(0, s.searchInsert([1, 3, 5, 6], 0))
        self.assertEqual(0, s.searchInsert([1, 3, 5, 6], 1))
        self.assertEqual(3, s.searchInsert([1, 3, 5, 6], 6))

        self.assertEqual(2, s.searchInsert([1, 3, 5, 6, 8], 5))
        self.assertEqual(1, s.searchInsert([1, 3, 5, 6, 8], 2))
        self.assertEqual(5, s.searchInsert([1, 3, 5, 6, 8], 9))
        self.assertEqual(0, s.searchInsert([1, 3, 5, 6, 8], 0))
        self.assertEqual(0, s.searchInsert([1, 3, 5, 6, 8], 1))
        self.assertEqual(4, s.searchInsert([1, 3, 5, 6, 8], 8))

        self.assertEqual(0, s.searchInsert([1, 2], 0))
        self.assertEqual(2, s.searchInsert([1, 2], 3))
        self.assertEqual(0, s.searchInsert([1, 2], 1))
        self.assertEqual(1, s.searchInsert([1, 2], 2))
        self.assertEqual(0, s.searchInsert([1], 0))
        self.assertEqual(1, s.searchInsert([1], 2))


if __name__ == "__main__":
    unittest.main()
