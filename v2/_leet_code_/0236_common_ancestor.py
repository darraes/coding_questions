class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.val == other.val

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        common, _, _ = self.lca(root, p, q)
        return common

    def lca(self, node, p, q):
        if not node:
            return None, False, False

        c_ancestor, l_found_p, l_found_q = self.lca(node.left, p, q)
        if c_ancestor:
            return c_ancestor, l_found_p, l_found_q

        c_ancestor, r_found_p, r_found_q = self.lca(node.right, p, q)
        if c_ancestor:
            return c_ancestor, r_found_p, r_found_q

        found_p = l_found_p or r_found_p or node == p
        found_q = l_found_q or r_found_q or node == q

        # print(node.val, found_p, found_q, p, q)

        return node if found_p and found_q else None, found_p, found_q


###############################################################
import unittest
from tree_utils import pretty_print, friendly_build, tree_equals


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        root = friendly_build(
            [
                ["1"],
                ["2", "3"],
                ["4", "5", "6", "7"],
                ["8", "9", "10", "11", "12", "13", "14", "15"],
            ]
        )

        common_ancestor = s.lowestCommonAncestor(root, TreeNode(8), TreeNode(10))
        self.assertEqual(2, common_ancestor.val)

        common_ancestor = s.lowestCommonAncestor(root, TreeNode(2), TreeNode(10))
        self.assertEqual(2, common_ancestor.val)

        common_ancestor = s.lowestCommonAncestor(root, TreeNode(1), TreeNode(10))
        self.assertEqual(1, common_ancestor.val)

        common_ancestor = s.lowestCommonAncestor(root, TreeNode(8), TreeNode(15))
        self.assertEqual(1, common_ancestor.val)

        common_ancestor = s.lowestCommonAncestor(root, TreeNode(8), TreeNode(3))
        self.assertEqual(1, common_ancestor.val)


if __name__ == "__main__":
    unittest.main()
