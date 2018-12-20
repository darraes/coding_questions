def search(x, matrix):
    row = 0
    col = len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == x:
            return (row, col)
        if x > matrix[row][col]:
            row += 1
        else:
            col -= 1

    return (-1, -1)


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        matrix = [
            [15, 20, 40, 85],
            [20, 35, 80, 95],
            [30, 55, 95, 105],
            [40, 80, 100, 120],
        ]
        self.assertEqual((0, 0), search(15, matrix))
        self.assertEqual((1, 3), search(95, matrix))
        self.assertEqual((-1, -1), search(99, matrix))


if __name__ == "__main__":
    unittest.main()
