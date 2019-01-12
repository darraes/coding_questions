from collections import Counter


class Solution:
    def neighbors_state(self, i, j, board):
        candidates = [
            (i - 1, j),
            (i, j - 1),
            (i + 1, j),
            (i, j + 1),
            (i - 1, j + 1),
            (i - 1, j - 1),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ]

        return Counter(
            [
                board[x][y]
                for (x, y) in candidates
                if 0 <= x < len(board) and 0 <= y < len(board[x])
            ]
        )

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        previous_round = []
        for row in board:
            previous_round.append([])
            for c in row:
                previous_round[-1].append(c)

        for i in range(len(previous_round)):
            for j in range(len(previous_round[i])):
                distribution = self.neighbors_state(i, j, previous_round)
                if previous_round[i][j] == 1:
                    if distribution[1] < 2:
                        # Any live cell with fewer than two live neighbors dies,
                        # as if caused by under-population.
                        board[i][j] = 0
                    if 2 <= distribution[1] <= 3:
                        # Any live cell with two or three live neighbors lives on
                        # to the next generation.
                        pass
                    if distribution[1] > 3:
                        # Any live cell with more than three live neighbors dies,
                        # as if by over-population.
                        board[i][j] = 0
                if previous_round[i][j] == 0:
                    if distribution[1] == 3:
                        # Any dead cell with exactly three live neighbors becomes a
                        # live cell, as if by reproduction.
                        board[i][j] = 1


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        answer = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        s.gameOfLife(board)
        self.assertEqual(answer, board)

        board = [[0]]
        answer = [[0]]
        s.gameOfLife(board)
        self.assertEqual(answer, board)

        board = [[1]]
        answer = [[0]]
        s.gameOfLife(board)
        self.assertEqual(answer, board)


if __name__ == "__main__":
    unittest.main()
