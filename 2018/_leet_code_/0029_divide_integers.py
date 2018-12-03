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

        return (
            res
            if (dividend <= 0 and divisor <= 0) or (dividend >= 0 and divisor >= 0)
            else neg_res
        )


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(5, s.divide(15, 3))
        self.assertEqual(5, s.divide(17, 3))


if __name__ == "__main__":
    unittest.main()
