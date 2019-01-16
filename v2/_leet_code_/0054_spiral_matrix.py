class Solution(object):
    def spiralOrder(self, matrix):
        def spiral_coords(row_s, col_s, row_e, col_e):
            for c in range(col_s, col_e + 1):
                yield row_s, c
            for r in range(row_s + 1, row_e + 1):
                yield r, col_e
            if row_s < row_e and col_s < col_e:
                for c in range(col_e - 1, col_s, -1):
                    yield row_e, c
                for r in range(row_e, row_s, -1):
                    yield r, col_s

        if not matrix:
            return []

        ans = []
        row_s, row_e = 0, len(matrix) - 1
        col_s, col_e = 0, len(matrix[0]) - 1
        while row_s <= row_e and col_s <= col_e:
            for r, c in spiral_coords(row_s, col_s, row_e, col_e):
                ans.append(matrix[r][c])
            row_s += 1
            row_e -= 1
            col_s += 1
            col_e -= 1
        return ans


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [3, 2],
            s.spiralOrder([[3],[2]]),
        )
        self.assertEqual(
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
            s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        )
        self.assertEqual(
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
        )


if __name__ == "__main__":
    unittest.main()
