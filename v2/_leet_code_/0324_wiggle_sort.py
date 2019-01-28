class Solution:
    def wiggleSort(self, nums):
        def swap(array, i, j):
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

        n = len(nums)
        m = (n + 1) // 2

        nums.sort()
        copy = [i for i in nums]

        i = m - 1
        j = 0
        while i >= 0:
            nums[j] = copy[i]
            i -= 1
            j += 2

        i = n - 1
        j = 1
        while i >= m:
            nums[j] = copy[i]
            i -= 1
            j += 2


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        nums = [1, 1, 1, 4, 5, 6]
        s.wiggleSort(nums)
        self.assertEqual([1, 6, 1, 5, 1, 4], nums)

        nums = [1, 1, 2, 2, 3, 3]
        s.wiggleSort(nums)
        self.assertEqual([2, 3, 1, 3, 1, 2], nums)


if __name__ == "__main__":
    unittest.main()
