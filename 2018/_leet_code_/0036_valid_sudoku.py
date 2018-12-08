class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Check line
        for i in range(len(board)):
            tracking = [False] * (len(board) + 1)
            for j in range(len(board[i])):
                element = board[i][j]
                if element != ".":
                    if tracking[int(element)]:
                        return False
                    else:
                        tracking[int(element)] = True

        # Check Column
        for i in range(len(board)):
            tracking = [False] * (len(board) + 1)
            for j in range(len(board[i])):
                element = board[j][i]
                if element != ".":
                    if tracking[int(element)]:
                        return False
                    else:
                        tracking[int(element)] = True

        # Check Squares
        square_starts = []
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                square_starts.append((i, j))
                j += 3
            i += 3
        
        for square in square_starts:
            tracking = [False] * (len(board) + 1)
            for i in range(square[0], square[0] + 3):
                for j in range(square[1], square[1] + 3):
                    element = board[i][j]
                    if element != ".":
                        if tracking[int(element)]:
                            return False
                        else:
                            tracking[int(element)] = True
        return True


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
        self.assertTrue(s.isValidSudoku(sudoku))

        sudoku = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertFalse(s.isValidSudoku(sudoku))

        s = Solution()
        sudoku = [
            ["9", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertFalse(s.isValidSudoku(sudoku))


if __name__ == "__main__":
    unittest.main()
