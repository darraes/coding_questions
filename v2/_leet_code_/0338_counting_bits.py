class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual([0, 1, 1], s.countBits(2))
        self.assertEqual([0, 1, 1, 2, 1, 2], s.countBits(5))


if __name__ == "__main__":
    unittest.main()
