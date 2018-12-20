def negate(n):
    operand = -1 if n > 0 else 1

    negation = 0
    while n != 0:
        n += operand
        negation += operand

    return negation


def subtraction(a, b):
    return a + negate(b)


def multiply(a, b):
    res = 0
    for i in range(abs(b)):
        res += a

    if a < 0 and b < 0 or a > 0 and b < 0:
        return negate(res)
    else:
        return res


def divide(a, b):
    res = 0
    absa = abs(a)
    absb = abs(b)

    while absb <= absa:
        res += 1
        absb += absb

    if a < 0 and b > 0 or a > 0 and b < 0:
        return negate(res)
    else:
        return res



###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(-3, negate(3))
        self.assertEqual(3, negate(-3))

        self.assertEqual(3, subtraction(6, 3))
        self.assertEqual(9, subtraction(6, -3))
        self.assertEqual(-3, subtraction(-6, -3))
        self.assertEqual(-9, subtraction(-6, 3))


        self.assertEqual(18, multiply(6, 3))
        self.assertEqual(-18, multiply(6, -3))
        self.assertEqual(18, multiply(-6, -3))
        self.assertEqual(-18, multiply(-6, 3))

        self.assertEqual(2, divide(6, 3))
        self.assertEqual(-2, divide(6, -3))
        self.assertEqual(2, divide(-6, -3))
        self.assertEqual(-2, divide(-6, 3))


if __name__ == '__main__':
    unittest.main()