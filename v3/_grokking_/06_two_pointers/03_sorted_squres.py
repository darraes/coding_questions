def make_squares(arr):
    if arr[0] >= 0:
        return [n * n for n in arr]

    squares = [-1 for n in arr]
    left, right, consumer = 0, len(arr) - 1, len(arr) - 1

    while consumer >= 0:
        l_square = arr[left] * arr[left]
        r_square = arr[right] * arr[right]

        if r_square > l_square:
            squares[consumer] = r_square
            right -= 1
        else:
            squares[consumer] = l_square
            left += 1

        consumer -= 1

    return squares


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual([0, 1, 4, 4, 9], make_squares([-2, -1, 0, 2, 3]))
        self.assertEqual([0, 1, 1, 4, 9], make_squares([-3, -1, 0, 1, 2]))
        self.assertEqual([0, 1, 4], make_squares([0, 1, 2]))
        self.assertEqual([1, 4, 9], make_squares([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
