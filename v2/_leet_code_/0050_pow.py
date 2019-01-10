class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return x * half * half


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(1024.0, s.myPow(2.0, 10))
        self.assertEqual(2048.0, s.myPow(2.0, 11))
        self.assertEqual(1, s.myPow(2.0, 0))
        self.assertEqual(2.0, s.myPow(2.0, 1))
        self.assertEqual(0.25, s.myPow(2.0, -2))


if __name__ == "__main__":
    unittest.main()
