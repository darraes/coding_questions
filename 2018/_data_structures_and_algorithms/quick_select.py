def quick_select(array, k):
    pivot = array[-1]

    c = 0
    for i, p in enumerate(array):
        print(i, p)

###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        k = quick_select([1, 4, 5, 2, 7, 8, 0, 9, 7, 2, 11, 34, 56, 15], 7)


if __name__ == "__main__":
    unittest.main()