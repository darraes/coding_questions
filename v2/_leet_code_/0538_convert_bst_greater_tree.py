# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        acc_val = 0

        def to_greater(node):
            nonlocal acc_val
            if not node:
                return

            to_greater(node.right)

            acc_val += node.val
            node.val = acc_val

            to_greater(node.left)

        to_greater(root)
        return root


###############################################################
import unittest
from tree_utils import serialize, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        problem = [5, 2, 13]
        self.assertEqual([18, 20, 13], serialize(s.convertBST(deserialize(problem))))

        problem = [10, 5, 20, 1, 7, None, 21]
        self.assertEqual(
            [51, 63, 41, 64, 58, None, 21],
            serialize(s.convertBST(deserialize(problem))),
        )

        problem = [5]
        self.assertEqual([5], serialize(s.convertBST(deserialize(problem))))

        problem = []
        self.assertEqual([], serialize(s.convertBST(deserialize(problem))))


if __name__ == "__main__":
    unittest.main()
