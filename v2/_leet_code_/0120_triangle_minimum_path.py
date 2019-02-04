class Solution:
    def minimumTotalRec(self, triangle):
        memo = {}

        def min_sum_from(row, col):
            nonlocal triangle, memo
            if col < 0 or (row < len(triangle) and col >= len(triangle[row])):
                return float("inf")

            if row == len(triangle):
                return 0

            if (row, col) not in memo:
                memo[(row, col)] = triangle[row][col] + min(
                    min_sum_from(row + 1, col), min_sum_from(row + 1, col + 1)
                )

            return memo[(row, col)]

        return min_sum_from(0, 0)

    def minimumTotal(self, triangle):
        dp = [n for n in triangle[-1]]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(0, row + 1):
                dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]

        return dp[0]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(-1, s.minimumTotal([[-1], [3, 2], [-3, 1, -1]]))
        self.assertEqual(11, s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
        self.assertEqual(2, s.minimumTotal([[2]]))


if __name__ == "__main__":
    unittest.main(exit=False)
