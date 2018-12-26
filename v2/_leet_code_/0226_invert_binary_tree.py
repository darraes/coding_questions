# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        left = root.left
        right = root.right

        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root


###############################################################
import unittest
from tree_utils import pretty_print, serialize, deserialize, tree_equals


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        problem = [-10, 9, 20, None, None, 15, 7]
        sol = [-10, 20, 9, 7, 15]
        self.assertEquals(sol, serialize(s.invertTree(deserialize(problem))))

        problem = [-10]
        sol = [-10]
        self.assertEquals(sol, serialize(s.invertTree(deserialize(problem))))

        problem = [-10, 9, 8]
        sol = [-10, 8, 9]
        self.assertEquals(sol, serialize(s.invertTree(deserialize(problem))))

        problem = [-10, 9]
        sol = [-10, None, 9]
        self.assertEquals(sol, serialize(s.invertTree(deserialize(problem))))


if __name__ == "__main__":
    unittest.main()
