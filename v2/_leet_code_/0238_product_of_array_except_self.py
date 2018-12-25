class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)

        left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] = nums[i] * left[i - 1]

        n = len(nums) - 1
        right[n] = nums[n]
        for i in range(n - 1, -1, -1):
            right[i] = nums[i] * right[i + 1]

        ans = []
        for i in range(len(nums)):
            mul = 1
            if i > 0:
                mul *= left[i - 1]
            if i < len(nums) - 1:
                mul *= right[i + 1]
            ans.append(mul)

        return ans


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([24, 12, 8, 6], s.productExceptSelf([1, 2, 3, 4]))
        self.assertEqual([1], s.productExceptSelf([3, 3]))
        self.assertEqual([3, 3], s.productExceptSelf([3]))


if __name__ == "__main__":
    unittest.main()
