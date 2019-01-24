class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            else:
                dp[i] += dp[i + 1]
                
            if i < len(s) - 1 and int(s[i: i + 2]) <= 26:
                dp[i] += dp[i + 2]

        return dp[0]



####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(0, s.numDecodings("0"))
        self.assertEqual(0, s.numDecodings("012"))
        self.assertEqual(0, s.numDecodings("027"))
        self.assertEqual(0, s.numDecodings("031"))
        self.assertEqual(1, s.numDecodings("120"))
        self.assertEqual(0, s.numDecodings("270"))
        self.assertEqual(1, s.numDecodings("310"))
        self.assertEqual(1, s.numDecodings("1"))
        self.assertEqual(2, s.numDecodings("12"))
        self.assertEqual(3, s.numDecodings("226"))
        self.assertEqual(3, s.numDecodings("6226"))
        self.assertEqual(5, s.numDecodings("1226"))


if __name__ == "__main__":
    unittest.main()