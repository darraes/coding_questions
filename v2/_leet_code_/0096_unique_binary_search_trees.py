class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        def _num_trees(nodes, i, j, lookup):
            if i >= j:
                return 1

            if (i, j) in lookup:
                return lookup[(i, j)]

            count = 0
            for root in range(i, j + 1):
                count += _num_trees(nodes, i, root - 1, lookup) * _num_trees(
                    nodes, root + 1, j, lookup
                )

            lookup[(i, j)] = count
            return count

        return _num_trees([p for p in range(n)], 0, n - 1, {})


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(5, s.numTrees(3))
        self.assertEqual(2, s.numTrees(2))
        self.assertEqual(42, s.numTrees(5))


if __name__ == "__main__":
    unittest.main()