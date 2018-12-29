class Solution:
    def __init__(self):
        self.lookup = []

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < len(self.lookup):
            return self.lookup[n]

        start = max(2, len(self.lookup))
        self.lookup.extend([2 ** 64 - 1] * (n + 1 - len(self.lookup)))
        self.lookup[0] = 0
        self.lookup[1] = 1

        for i in range(start, n + 1):
            j = 1
            while j * j <= n:
                self.lookup[i] = min(self.lookup[i], self.lookup[i - j * j] + 1)
                j += 1
        return self.lookup[-1]


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
        self.assertEqual(3, s.numSquares(4635))
        self.assertEqual(3, s.numSquares(4635))
        self.assertEqual(2, s.numSquares(1000))


if __name__ == "__main__":
    unittest.main()
