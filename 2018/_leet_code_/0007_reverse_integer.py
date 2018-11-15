class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2**31-1
        min_int = -2**31

        res = 0
        signal = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            res *= 10
            res += x % 10
            x = int(x / 10)
        res = res * signal
        return res if res <= max_int and res >= min_int else 0


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(321, s.reverse(123))
        self.assertEqual(4321, s.reverse(1234))
        self.assertEqual(21, s.reverse(12))
        self.assertEqual(2, s.reverse(2))
        self.assertEqual(0, s.reverse(0))
        self.assertEqual(-321, s.reverse(-123))
        self.assertEqual(-4321, s.reverse(-1234))
        self.assertEqual(-21, s.reverse(-12))
        self.assertEqual(-2, s.reverse(-2))
        self.assertEqual(0, s.reverse(1534236469))


if __name__ == '__main__':
    unittest.main()