class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0

        while True:
            count = 1
            while (res + count) ** 2 <= x:
                count *= 2

            if count == 1:
                break

            res += count // 2

        return res




###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(5, s.mySqrt(25))
        self.assertEqual(4, s.mySqrt(24))
        self.assertEqual(4, s.mySqrt(16))
        self.assertEqual(4, s.mySqrt(17))
        self.assertEqual(2, s.mySqrt(8))
        self.assertEqual(1, s.mySqrt(3))
        self.assertEqual(1, s.mySqrt(2))


if __name__ == '__main__':
    unittest.main()