class Solution:
    def getMoneyAmount(self, n: "int") -> "int":
        memo = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        def calc(s, e):
            nonlocal memo

            if s >= e:
                return 0

            if memo[s][e] is None:
                ans = float("inf")
                for i in range(s, e + 1):
                    ans = min(ans, i + max(calc(s, i - 1), calc(i + 1, e)))
                memo[s][e] = ans
            return memo[s][e]

        return calc(1, n)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(6, s.getMoneyAmount(5))
        self.assertEqual(12, s.getMoneyAmount(8))


if __name__ == "__main__":
    unittest.main(exit=False)
