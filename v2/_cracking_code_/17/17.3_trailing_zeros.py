def count_5s(n):
    res = 0
    i = 5
    while n / i > 0:
        res += int(n / i)
        i *= 5
    return res


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, count_5s(5))
        self.assertEqual(3, count_5s(15))
        self.assertEqual(3, count_5s(17))


if __name__ == "__main__":
    unittest.main()