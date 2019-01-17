class Solution:
    def generateMatrix(self, n):
        def spiral_next(row_s, row_e, col_s, col_e):
            for c in range(col_s, col_e + 1):
                yield row_s, c
            for r in range(row_s + 1, row_e + 1):
                yield r, col_e
            if col_e > col_s and row_e > row_s:
                for c in range(col_e - 1, col_s - 1, -1):
                    yield row_e, c
                for r in range(row_e - 1, row_s, -1):
                    yield r, col_s

        res = [[0 for _ in range(n)] for _ in range(n)]
        row_s, row_e = 0, n - 1
        col_s, col_e = 0, n - 1
        number = 1
        while row_s <= row_e and col_s <= col_e:
            for x, y in spiral_next(row_s, row_e, col_s, col_e):
                res[x][y] = number
                number += 1
            row_s += 1
            row_e -= 1
            col_s += 1
            col_e -= 1

        return res


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([[1]], s.generateMatrix(1))
        self.assertEqual([[1, 2], [4, 3]], s.generateMatrix(2))
        self.assertEqual([[1, 2, 3], [8, 9, 4], [7, 6, 5]], s.generateMatrix(3))


if __name__ == "__main__":
    unittest.main()
