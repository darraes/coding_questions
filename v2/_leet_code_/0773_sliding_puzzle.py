from collections import deque
from itertools import chain


class Solution:
    RIGHT_ALLOWED = set([0, 1, 3, 4])
    LEFT_ALLOWED = set([1, 2, 4, 5])

    def solved(self, board):
        return board == (1, 2, 3, 4, 5, 0)

    def next(self, state):
        zero_idx = state[0]
        board = state[1]

        next_boards = []

        def copy():
            nonlocal board
            return [e for e in board]

        def swap(b, i, j):
            tmp = b[i]
            b[i] = b[j]
            b[j] = tmp

        n = copy()
        swap(n, zero_idx, (zero_idx + 3) % 6)
        next_boards.append(((zero_idx + 3) % 6, tuple(n)))

        if zero_idx in Solution.RIGHT_ALLOWED:
            n = copy()
            swap(n, zero_idx, zero_idx + 1)
            next_boards.append((zero_idx + 1, tuple(n)))

        if zero_idx in Solution.LEFT_ALLOWED:
            n = copy()
            swap(n, zero_idx, zero_idx - 1)
            next_boards.append((zero_idx - 1, tuple(n)))

        return next_boards

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        current = tuple(chain(*board))
        visited = set([current])
        zero_idx = None
        for i in range(len(current)):
            if current[i] == 0:
                zero_idx = i
                break

        queue = deque([(zero_idx, current, 0)])

        while len(queue) > 0:
            zero_idx, current, moves = queue.popleft()

            if self.solved(current):
                return moves

            for z_idx, n_board in self.next((zero_idx, current)):
                if n_board not in visited:
                    visited.add(n_board)
                    queue.append((z_idx, n_board, moves + 1))

        return -1


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("=================START=================")
        s = Solution()
        board = [[3, 2, 4], [1, 5, 0]]
        self.assertEqual(14, s.slidingPuzzle(board))

        board = [[1, 2, 3], [5, 4, 0]]
        self.assertEqual(-1, s.slidingPuzzle(board))

        board = [[1, 2, 3], [4, 0, 5]]
        self.assertEqual(1, s.slidingPuzzle(board))

        board = [[1, 2, 3], [4, 5, 0]]
        self.assertEqual(0, s.slidingPuzzle(board))

        board = [[0, 2, 3], [4, 1, 5]]
        self.assertEqual(-1, s.slidingPuzzle(board))


if __name__ == "__main__":
    unittest.main()
