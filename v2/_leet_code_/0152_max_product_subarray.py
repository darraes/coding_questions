class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gmax = cmax = cmin = nums[0]
        for i in range(1, len(nums)):
            cmax, cmin = (
                max(nums[i], cmax * nums[i], cmin * nums[i]),
                min(nums[i], cmax * nums[i], cmin * nums[i]),
            )
            gmax = max(cmax, gmax)
        return gmax


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(6, s.maxProduct([2, 3, -2, 4]))
        self.assertEqual(0, s.maxProduct([-2, 0, -1]))
        self.assertEqual(8, s.maxProduct([2, 3, -2, 4, 2]))
        self.assertEqual(96, s.maxProduct([2, 3, -2, 4, 2, -1]))


if __name__ == "__main__":
    unittest.main()
