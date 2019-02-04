class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        memo = [[None for _ in range(n)] for _ in range(n)]

        def generate(nodes, s, e):
            if s > e:
                return [None]
            if memo[s][e]:
                return memo[s][e]

            res = []
            for i in range(s, e + 1):
                lefts = generate(nodes, s, i - 1)
                rights = generate(nodes, i + 1, e)
                for l in lefts:
                    for r in rights:
                        node = TreeNode(nodes[i])
                        node.left = l
                        node.right = r

                        res.append(node)

            memo[s][e] = res
            return res

        return generate([i + 1 for i in range(n)], 0, n - 1)


###############################################################
import unittest
from tree_utils import pretty_print, serialize, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        def convert(ar):
            return set([tuple(t) for t in ar])

        self.assertEqual(
            convert(
                [
                    [1, None, 3, 2],
                    [3, 2, None, 1],
                    [3, 1, None, None, 2],
                    [2, 1, 3],
                    [1, None, 2, None, 3],
                ]
            ),
            convert([serialize(t) for t in s.generateTrees(3)]),
        )

        self.assertEqual(
            convert([[1]]), convert([serialize(t) for t in s.generateTrees(1)])
        )

        self.assertEqual(
            convert([]), convert([serialize(t) for t in s.generateTrees(0)])
        )


if __name__ == "__main__":
    unittest.main(exit=False)
