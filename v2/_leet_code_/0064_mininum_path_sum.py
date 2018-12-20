def print_lines(X):
    for x in X:
        print(x)
    print("============")


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def non_negative_min(x, y):
            if x < 0:
                return y
            if y < 0:
                return x
            return min(x, y)

        m = len(grid)
        n = len(grid[0])
        lookup = [[-1 for j in range(n + 1)] for i in range(m + 1)]
        lookup[1][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                lookup[i][j] = grid[i - 1][j - 1] + non_negative_min(
                    lookup[i - 1][j], lookup[i][j - 1]
                )

        return lookup[-1][-1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(7, s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
        self.assertEqual(
            63,
            s.minPathSum(
                [
                    [0, 2, 2, 6, 4, 1, 6, 2, 9, 9, 5, 8, 4, 4],
                    [0, 3, 6, 4, 5, 5, 9, 7, 8, 3, 9, 9, 5, 4],
                    [6, 9, 0, 7, 2, 2, 5, 6, 3, 1, 0, 4, 2, 5],
                    [3, 8, 2, 3, 2, 8, 8, 7, 5, 9, 6, 3, 4, 5],
                    [4, 0, 1, 3, 9, 2, 0, 1, 6, 7, 9, 2, 8, 9],
                    [6, 2, 7, 9, 0, 9, 5, 2, 7, 5, 1, 4, 4, 7],
                    [9, 8, 3, 3, 0, 6, 8, 0, 8, 8, 3, 5, 7, 3],
                    [7, 7, 4, 5, 9, 1, 5, 0, 2, 2, 2, 1, 7, 4],
                    [5, 1, 3, 4, 1, 6, 0, 4, 3, 8, 4, 3, 9, 9],
                    [0, 6, 4, 9, 4, 1, 5, 5, 4, 2, 5, 7, 4, 0],
                    [0, 1, 6, 6, 4, 9, 2, 7, 8, 2, 1, 3, 3, 7],
                    [8, 4, 9, 9, 2, 3, 8, 6, 6, 5, 4, 1, 7, 9],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
