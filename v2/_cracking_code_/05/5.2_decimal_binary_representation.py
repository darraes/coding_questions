def binary_representation(n, precision = 32):
    if n >= 1 or n < 0:
        return None

    binary = "0."
    frac = 0.5
    digits = 0

    while n > 0 and digits < precision:
        if n >= frac:
            binary += "1"
            n -= frac
        else:
            binary += "0"
        frac /= 2
        digits += 1
    return binary


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual("0.01111", binary_representation(0.47, 5))
        self.assertEqual("0.11111100", binary_representation(0.986, 8))


if __name__ == '__main__':
    unittest.main()