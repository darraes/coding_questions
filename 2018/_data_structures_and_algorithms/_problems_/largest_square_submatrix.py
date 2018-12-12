def print_lines(X):
    for x in X:
        print(x)


def largest_square_submatrix(M):
    m = len(M)
    n = len(M[0])
    lookup = [[0 for y in range(len(M[0]) + 1)] for x in range(len(M) + 1)]
    max_area = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if M[i - 1][j - 1] == 0:
                lookup[i][j] = 0
            else:
                lookup[i][j] = 1 + min(
                    lookup[i - 1][j - 1], lookup[i - 1][j], lookup[i][j - 1]
                )
                max_area = max(max_area, lookup[i][j])

    print_lines(lookup)
    return max_area


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
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
        self.assertEqual(3, largest_square_submatrix(matrix))


if __name__ == "__main__":
    unittest.main()
