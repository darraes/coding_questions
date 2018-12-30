class Solution:
    lookup = []

    @classmethod
    def numSquares(cls, n):
        """
        :type n: int
        :rtype: int
        """
        if n < len(cls.lookup):
            return cls.lookup[n]

        start = max(2, len(cls.lookup))
        cls.lookup.extend([2 ** 64 - 1] * (n + 1 - len(cls.lookup)))
        cls.lookup[0] = 0
        cls.lookup[1] = 1

        for i in range(start, n + 1):
            j = 1
            while j * j <= n:
                cls.lookup[i] = min(cls.lookup[i], cls.lookup[i - j * j] + 1)
                j += 1
        return cls.lookup[-1]


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
