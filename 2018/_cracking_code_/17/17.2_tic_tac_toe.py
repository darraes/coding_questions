def victory(board):
    for line in range(3):
        won = True
        candidate = board[line][0]
        if candidate is None:
            continue
        for column in range(1, 3):
            if candidate != board[line][column]:
                won = False
                break
        if won:
            return True

    for column in range(3):
        won = True
        candidate = board[0][column]
        if candidate is None:
            continue
        for line in range(1, 3):
            if candidate != board[line][column]:
                won = False
                break
        if won:
            return True

    return board[0][0] == board[1][1] == board[2][2] \
        or board[0][2] == board[1][1] == board[2][0]


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertTrue(victory([
            [0, None, None],
            [1, 1, 1],
            [None, 0, 0]
        ]))
        self.assertTrue(victory([
            [0, 1, None],
            [1, 1, 0],
            [None, 1, 0]
        ]))
        self.assertTrue(victory([
            [0, 1, None],
            [1, 0, 0],
            [None, 1, 0]
        ]))
        self.assertFalse(victory([
            [0, 1, None],
            [1, 0, 0],
            [None, 1, 1]
        ]))


if __name__ == "__main__":
    unittest.main()