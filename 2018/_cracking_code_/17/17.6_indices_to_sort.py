def find_left(array):
    i = 0
    while i < len(array):
        if i == len(array) - 1 or array[i] > array[i + 1]:
            break
        i += 1
    return i


def find_right(array):
    i = len(array) - 1
    while i >= 0:
        if i == 0 or array[i] < array[i - 1]:
            break
        i -= 1
    return i


def find_min_max(array, left, right):
    _min = min(array[left], array[right])
    _max = max(array[left], array[right])

    for i in range(right):
        if array[i] > _max:
            _max = array[i]
    for i in range(left, len(array)):
        if array[i] < _min:
            _min = array[i]

    return _min, _max


def find_indexes(array):
    max_left = find_left(array)
    min_right = find_right(array)

    if max_left == len(array) - 1:
        return (-1, -1)

    _min, _max = find_min_max(array, max_left, min_right)

    while max_left >= 0 and array[max_left] > _min:
        max_left -= 1

    while min_right < len(array) and array[min_right] < _max:
        min_right += 1

    return max_left + 1, min_right - 1


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            (3, 9), find_indexes([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
        self.assertEqual(
            (-1, -1), find_indexes([1, 2, 4, 7, 10, 11]))
        self.assertEqual(
            (2, 8), find_indexes([1, 2, 4, 7, 10, 2, 3, 4, 7]))
        self.assertEqual(
            (1, 9), find_indexes([1, 2, 4, 7, 10, 2, 3, 1, 4, 7]))


if __name__ == "__main__":
    unittest.main()