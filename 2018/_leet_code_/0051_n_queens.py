class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self._solve([-1] * n, 0, n, res)

        ans = []
        for r in res:
            ans.append([])
            for e in r:
                code = ["."] * n
                code[e] = "Q"
                ans[-1].append("".join(code))

        return ans

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
        self.assertEqual([], s.solveNQueens(0))
        self.assertEqual([["Q"]], s.solveNQueens(1))
        self.assertEqual([], s.solveNQueens(2))
        self.assertEqual([], s.solveNQueens(3))
        self.assertEqual(
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
            s.solveNQueens(4),
        )
        self.assertEqual(
            [
                ["Q....", "..Q..", "....Q", ".Q...", "...Q."],
                ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
                [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
                [".Q...", "....Q", "..Q..", "Q....", "...Q."],
                ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
                ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
                ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
                ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
                ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
                ["....Q", "..Q..", "Q....", "...Q.", ".Q..."],
            ],
            s.solveNQueens(5),
        )


if __name__ == "__main__":
    unittest.main()
