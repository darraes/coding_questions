def _search(x, array, s, e):
    mid = (s + e) // 2

    if array[mid] == x:
        return mid

    if s > e:
        return -1

    if array[s] < array[mid]:
        if array[s] <= x < array[mid]:
            return _search(x, array, s, mid - 1)
        else:
            return _search(x, array, mid + 1, e)
    else:
        if array[mid] < x <= array[e]:
            return _search(x, array, mid + 1, e)
        else:
            return _search(x, array, s, mid - 1)


def search(x, array):
    return _search(x, array, 0, len(array) - 1)


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, search(1, [1, 2, 3, 4]))
        self.assertEqual(3, search(1, [5, 6, 7, 1, 2, 3, 4]))
        self.assertEqual(6, search(4, [5, 6, 7, 1, 2, 3, 4]))
        self.assertEqual(0, search(5, [5, 6, 7, 1, 2, 3, 4]))
        self.assertEqual(2, search(7, [5, 6, 7, 1, 2, 3, 4]))
        self.assertEqual(-1, search(3, [4, 5, 6, 7, 0, 1, 2]))
        self.assertEqual(-1, search(4, [5, 6, 7, 0, 1, 2]))
        self.assertEqual(0, search(1, [1]))
        self.assertEqual(-1, search(2, [1]))
        self.assertEqual(0, search(2, [2, 1]))
        self.assertEqual(1, search(2, [1, 2]))
        self.assertEqual(1, search(5, [3, 5, 1]))


if __name__ == "__main__":
    unittest.main()
