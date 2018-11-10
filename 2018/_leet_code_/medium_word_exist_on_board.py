# https://leetcode.com/problems/word-search/description/

class Solution(object):
    def in_board(self, point, board):
        if point[0] < 0 or point[0] >= len(board):
            return False
        if point[1] < 0 or point[1] >= len(board[point[0]]):
            return False
        return True


    def adjacents(self, start, board):
        result = [
            (start[0] + 1, start[1]),
            (start[0] - 1, start[1]),
            (start[0], start[1] + 1),
            (start[0], start[1] - 1)
        ]

        return [r for r in result if self.in_board(r, board)]


    def is_word_start(self, word, board, current, visiting):
        if current[0] >= len(word):
            return False

        if word[current[0]] == board[current[1][0]][current[1][1]]:
            if current[0] == len(word) - 1:
                return True

            visiting.add(current[1])
            for adj in [a for a in self.adjacents(current[1], board) 
                        if a not in visiting]:
                found = self.is_word_start(
                    word, board, (current[0] + 1, adj), visiting)
                if found:
                    return True
            visiting.remove(current[1])
        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                found = self.is_word_start(word, board, (0, (i, j)), set())
                if found :
                    return True
        return False


    ####### =============== TESTS =============== 
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        board =[
                  ['A','B','C','E'],
                  ['S','F','C','S'],
                  ['A','D','E','E']
               ]

        s = Solution()
        self.assertTrue(s.exist(board, "ABCCED"))
        self.assertTrue(s.exist(board, "ECBA"))
        self.assertTrue(s.exist(board, "SEE"))
        self.assertFalse(s.exist(board, "ABCB"))
        self.assertFalse(s.exist(board, "ECD"))

    def test_2(self):
        board =[
                  ['A']
               ]

        s = Solution()
        self.assertTrue(s.exist(board, "A"))
        self.assertFalse(s.exist(board, "B"))

    def test_3(self):
        board =[
                  ['A','B','C','E'],
                  ['S','F','C'],
                  ['A','D','E','E']
               ]

        s = Solution()
        self.assertTrue(s.exist(board, "ABCCED"))
        self.assertFalse(s.exist(board, "SEE"))
        self.assertFalse(s.exist(board, "ABCB"))


if __name__ == '__main__':
    unittest.main()