class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
            
        dp = [
            [0 for _ in range(len(obstacleGrid[0]) + 1)]
            for _ in range(len(obstacleGrid) + 1)
        ]

        dp[1][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(0, s.uniquePathsWithObstacles([[1]]))
        self.assertEqual(1, s.uniquePathsWithObstacles([[0]]))
        self.assertEqual(
            2, s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        )

        self.assertEqual(
            3, s.uniquePathsWithObstacles([[0, 0, 0], 
                                           [0, 0, 1],
                                           [0, 0, 0]])
        )


if __name__ == "__main__":
    unittest.main()
