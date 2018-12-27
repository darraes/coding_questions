class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        lookup = [2 ** 64 - 1] * (n + 1)
        lookup[0] = 0
        lookup[1] = 1

        for i in range(2, n + 1):
            j = 1
            while j * j <= n:
                lookup[i] = min(lookup[i], lookup[i - j * j] + 1)
                j += 1
        return lookup[-1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.numSquares(3))
        self.assertEqual(2, s.numSquares(2))
        self.assertEqual(1, s.numSquares(4))
        self.assertEqual(2, s.numSquares(5))
        self.assertEqual(3, s.numSquares(12))
        self.assertEqual(2, s.numSquares(13))


if __name__ == "__main__":
    unittest.main()
