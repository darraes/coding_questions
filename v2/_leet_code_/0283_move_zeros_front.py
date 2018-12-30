class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        c = p = 0
        while p < len(nums):
            if nums[p] != 0:
                tmp = nums[c]
                nums[c] = nums[p]
                nums[p] = tmp
                c += 1
            p += 1

        return nums


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([1, 3, 12, 0, 0], s.moveZeroes([0, 1, 0, 3, 12]))
        self.assertEqual([], s.moveZeroes([]))
        self.assertEqual([0], s.moveZeroes([0]))
        self.assertEqual([0, 0], s.moveZeroes([0, 0]))


if __name__ == "__main__":
    unittest.main()
