class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = 0
        def _solve(board, i, n):
            nonlocal res
            if i == len(board):
                res += 1
                return

            for c in self._candidates(board, i, n):
                board[i] = c
                _solve(board, i + 1, n)
        _solve([-1] * n, 0, n)
        return res

    

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
