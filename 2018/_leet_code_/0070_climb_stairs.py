class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0] * (n + 1)
        if n >= 1:
            dp[1] = 1
        if n >= 2:
            dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.climbStairs(3))
        self.assertEqual(2, s.climbStairs(2))
        self.assertEqual(1, s.climbStairs(1))
        self.assertEqual(0, s.climbStairs(0))


if __name__ == "__main__":
    unittest.main()
