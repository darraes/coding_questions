class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.dp = [0] * len(nums)
        if len(nums) > 0:
            self.dp[0] = nums[0]
            for i in range(1, len(nums)):
                self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i, j):
        if i < 0 or i >= len(self.nums) or j < 0 or j >= len(self.nums) or i > j:
            return None
        return self.dp[j] - self.dp[i] + self.nums[i]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(1, s.sumRange(0, 2))
        self.assertEqual(-1, s.sumRange(2, 5))
        self.assertEqual(-3, s.sumRange(0, 5))


if __name__ == "__main__":
    unittest.main(exit=False)
