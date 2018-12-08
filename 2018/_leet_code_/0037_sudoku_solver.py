from copy import deepcopy


class Solution:
    NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def _list_possibilities(self, board, row, col):
        used = set()
        for i in range(9):
            used.add(board[row][i])
            used.add(board[i][col])

        square_r = int(row / 3)
        square_c = int(col / 3)
        for row in range(3 * square_r, 3 * square_r + 3):
            for col in range(3 * square_c, 3 * square_c + 3):
                used.add(board[row][col])

        return [p for p in Solution.NUMBERS if p not in used]

    def _solve(self, problem, board, row, col):
        possibilities = [problem[row][col]]
        if problem[row][col] == ".":
            possibilities = self._list_possibilities(board, row, col)

        for p in possibilities:
            board[row][col] = p

            if row == 8 and col == 8:
                return True

            n_row, n_col = self._next(row, col)
            if self._solve(problem, board, n_row, n_col):
                return True

        if problem[row][col] == ".":
            board[row][col] = "."
        return False

    def _next(self, i, j):
        if j < 8:
            return i, j + 1
        else:
            return i + 1, 0

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        problem = deepcopy(board)
        self._solve(problem, board, 0, 0)


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        sudoku = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        s.solveSudoku(sudoku)
        for l in sudoku:
            print(l)


if __name__ == "__main__":
    unittest.main()
