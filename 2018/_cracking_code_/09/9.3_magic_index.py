def find_magic_index(array):
    def _find_magic_index(array, s, e):
        if s > e:
            return -1

        i = int((s + e) / 2)
        if array[i] == i:
            return i

        if i > array[i]:
            return _find_magic_index(array, i + 1, e)
        else:
            return _find_magic_index(array, s, i - 1)
    return _find_magic_index(array, 0, len(array) - 1)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(7, find_magic_index([-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]))


if __name__ == "__main__":
    unittest.main()
