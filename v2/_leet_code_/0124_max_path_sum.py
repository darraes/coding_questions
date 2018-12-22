# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes fro
# some starting node to any node in the tree along the parent-child
# connections. The path must contain at least one node and does not
# need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42
import sys


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_so_far = -sys.maxsize - 1

        def _max_sum(node):
            nonlocal max_so_far

            if node is None:
                return 0

            left = max(0, _max_sum(node.left))
            right = max(0, _max_sum(node.right))

            max_so_far = max(max_so_far, left + right + node.val)
            return max(left, right) + node.val

        _max_sum(root)
        return max_so_far


###############################################################
import unittest
from tree_utils import TreeNode, pretty_print, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            48,
            s.maxPathSum(
                deserialize([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
            ),
        )
        self.assertEqual(3, s.maxPathSum(deserialize([1, -2, -3, 1, 3, -2, None, -1])))
        self.assertEqual(3, s.maxPathSum(deserialize([1, -2, -3, 1, 3, -2, None, -1])))
        self.assertEqual(42, s.maxPathSum(deserialize([-10, 9, 20, None, None, 15, 7])))
        self.assertEqual(6, s.maxPathSum(deserialize([1, 2, 3])))
        self.assertEqual(6, s.maxPathSum(deserialize([6, -2, -3])))
        self.assertEqual(-3, s.maxPathSum(deserialize([-3])))


if __name__ == "__main__":
    unittest.main()
