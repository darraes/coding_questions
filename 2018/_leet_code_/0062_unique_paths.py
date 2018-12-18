class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        lookup = [[0 for j in range(n + 1)] for i in range(m + 1)]
        lookup[1][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                lookup[i][j] = lookup[i - 1][j] + lookup[i][j - 1]

        return lookup[-1][-1]



###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.uniquePaths(3, 2))
        self.assertEqual(28, s.uniquePaths(7, 3))

if __name__ == "__main__":
    unittest.main()