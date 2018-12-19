def print_lines(X):
    for x in X:
        print(x)
    print("============")


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        if n == 0:
            return m
        if m == 0:
            return n

        lookup = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(m + 1):
            lookup[i][0] = i

        for j in range(n + 1):
            lookup[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0
                if word1[i - 1] != word2[j - 1]:
                    cost = 1

                lookup[i][j] = min(
                    cost + lookup[i - 1][j - 1],
                    lookup[i][j - 1] + 1,
                    lookup[i - 1][j] + 1,
                )
        return lookup[-1][-1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.minDistance("horse", "ros"))


if __name__ == "__main__":
    unittest.main()
