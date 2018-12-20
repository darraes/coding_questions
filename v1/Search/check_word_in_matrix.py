# http://www.careercup.com/question?id=5890898499993600

# Given a matrix of letters and a word, check if the word is present in the matrix. E,g., suppose matrix is: 
# a b c d e f 
# z n a b c f 
# f g f a b c 
# and given word is fnz, it is present. However, gng is not since you would be repeating g twice. 
# You can move in all the 8 directions around an element

def adjacents(matrix, x, y):
    return [point for point in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1)] \
        if point[0] >= 0 and point[0] < len(matrix) and point[1] >= 0 and point[1] < len(matrix[0])]


def _find(matrix, start_x, start_y, word, i_letter, visited):
    if i_letter == len(word): return True

    #Set is used to make sure we don't use the same position twice
    visited.add((start_x, start_y))    

    adjs = adjacents(matrix, start_x, start_y)

    for point in adjs:
        if matrix[point[0]][point[1]] == word[i_letter] \
          and (point[0], point[1]) not in visited:
            sub_result = _find(matrix, point[0], point[1], word, i_letter + 1, visited)
            if sub_result: 
                return True
 
    visited.remove((start_x, start_y))
    return False


def find(matrix, word):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == word[0]:
                tmp_result = _find(matrix, i, j, word, 1, set())
                if tmp_result: return True
    return False



###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_basic(self):
        matr = [["a", "b", "c", "d", "e", "f"],
                ["z", "n", "a", "b", "c", "f"],
                ["f", "g", "f", "a", "b", "c"]]

        self.assertEqual(True, find(matr, "fnz"))
        self.assertEqual(True, find(matr, "facef"))
        self.assertEqual(False, find(matr, "bola"))

    def test_loop(self):
        matr = [["a", "b", "c", "d", "e", "f"],
                ["z", "n", "a", "x", "c", "f"],
                ["f", "g", "f", "a", "b", "c"]]

        self.assertEqual(False, find(matr, "abcb"))
        self.assertEqual(True, find(matr, "fcf"))

if __name__ == '__main__':
    unittest.main()