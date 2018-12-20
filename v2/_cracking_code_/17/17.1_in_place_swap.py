def in_place_swap(a, b):
    a = a - b
    b = a + b
    a = b - a

    return (a, b)

####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual((3, 9), in_place_swap(9, 3))


if __name__ == "__main__":
    unittest.main()