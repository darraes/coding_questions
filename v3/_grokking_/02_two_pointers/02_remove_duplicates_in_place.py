def remove_duplicates(arr):
    c = 1

    for p in range(1, len(arr)):
        if arr[p] > arr[c - 1]:
            arr[c] = arr[p]
            c += 1

    return c


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
        self.assertEqual(2, remove_duplicates([2, 2, 2, 11]))

if __name__ == "__main__":
    unittest.main()