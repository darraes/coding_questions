class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        neg_res = 0
        _dividend = abs(dividend)
        _divisor = abs(divisor)

        max_int = 2 ** 31 - 1
        min_int = -1 * 2 ** 31

        while _dividend >= _divisor:
            div = _divisor
            count = 1

            while div <= _dividend:
                div = div << 1
                count *= 2

            count /= 2
            div >>= 1

            res += count
            neg_res -= count
            _dividend -= div

        if res > max_int:
            res = max_int
        if neg_res < min_int:
            neg_res = min_int

        return (
            int(res)
            if (dividend <= 0 and divisor <= 0) or (dividend >= 0 and divisor >= 0)
            else int(neg_res)
        )


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(5, s.divide(15, 3))
        self.assertEqual(5, s.divide(17, 3))
        self.assertEqual(17, s.divide(17, 1))
        self.assertEqual(2 ** 31 - 1, s.divide(2 ** 34, 1))
        self.assertEqual(-2 ** 31, s.divide(2 ** 34, -1))
        self.assertEqual(-17, s.divide(17, -1))
        self.assertEqual(-5, s.divide(17, -3))
        self.assertEqual(-5, s.divide(-17, 3))


if __name__ == "__main__":
    unittest.main()
