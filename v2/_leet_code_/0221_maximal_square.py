def print_lines(X):
    for x in X:
        print(x)


class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        lookup = [
            [0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)
        ]

        max_area = 0
        for i in range(1, len(lookup)):
            for j in range(1, len(lookup[i])):
                if matrix[i - 1][j - 1] == 0 or matrix[i - 1][j - 1] == "0":
                    lookup[i][j] = 0
                else:
                    lookup[i][j] = 1 + min(
                        lookup[i - 1][j], lookup[i][j - 1], lookup[i - 1][j - 1]
                    )
                    max_area = max(max_area, lookup[i][j] ** 2)
        return max_area


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        matrix = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
        self.assertEqual(4, s.maximalSquare(matrix))

        matrix = [
            [0, 0, 1, 0, 1, 1],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 0],
            [1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
        ]
        self.assertEqual(9, s.maximalSquare(matrix))

        matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
        self.assertEqual(4, s.maximalSquare(matrix))

        matrix = [[1]]
        self.assertEqual(1, s.maximalSquare(matrix))

        matrix = [[1, 1], [1, 1]]
        self.assertEqual(4, s.maximalSquare(matrix))

        matrix = [[1, 0], [1, 1]]
        self.assertEqual(1, s.maximalSquare(matrix))

        matrix = [[]]
        self.assertEqual(0, s.maximalSquare(matrix))

        matrix = [[0]]
        self.assertEqual(0, s.maximalSquare(matrix))


if __name__ == "__main__":
    unittest.main()
