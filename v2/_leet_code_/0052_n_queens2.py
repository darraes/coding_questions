class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self._solve([-1] * n, 0, n, res)
        return len(res)

    def _solve(self, board, i, n, results):
        if i == len(board):
            results.append([] + board)
            return

        for c in self._candidates(board, i, n):
            board[i] = c
            self._solve(board, i + 1, n, results)

    def _candidates(self, board, i, n):
        candidates = set([c for c in range(n)])

        for j in range(i):
            if board[j] in candidates:
                candidates.remove(board[j])
            if board[j] + (i - j) in candidates:
                candidates.remove(board[j] + (i - j))
            if board[j] - (i - j) in candidates:
                candidates.remove(board[j] - (i - j))

        return candidates

###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(1, s.totalNQueens(0))
        self.assertEqual(1, s.totalNQueens(1))
        self.assertEqual(0, s.totalNQueens(2))
        self.assertEqual(0, s.totalNQueens(3))
        self.assertEqual(2, s.totalNQueens(4))
        self.assertEqual(10, s.totalNQueens(5))


if __name__ == "__main__":
    unittest.main()
