class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        e = len(nums) - 1
        while True:
            m = self.quick_partition(nums, s, e)
            
            if m == k - 1:
                return nums[m]
            elif m < k - 1:
                s = m + 1
            else:
                e = m - 1

    def quick_partition(self, nums, s, e):
        mid = (s + e) // 2
        pivot = nums[mid]
        self.swap(nums, mid, e)

        c = p = s
        for p in range(s, e + 1):
            if nums[p] > pivot:
                self.swap(nums, c, p)
                c += 1

        self.swap(nums, c, e)
        return c


    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp


###############################################################


import unittest
from random import shuffle


class TestFunctions(unittest.TestCase):
    def test_quickselect(self):
        s = Solution()
        array = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        shuffle(array)
        self.assertEqual(14, s.findKthLargest(array, 7))
        self.assertEqual(20, s.findKthLargest(array, 1))
        self.assertEqual(11, s.findKthLargest(array, 10))

        array = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        shuffle(array)
        self.assertEqual(15, s.findKthLargest(array, 7))
        self.assertEqual(21, s.findKthLargest(array, 1))
        self.assertEqual(12, s.findKthLargest(array, 10))
        self.assertEqual(11, s.findKthLargest(array, 11))

        array = [11]
        self.assertEqual(11, s.findKthLargest(array, 1))


if __name__ == "__main__":
    unittest.main()
