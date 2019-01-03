class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False

        if s.val == t.val and self.is_exact_subtree(s, t):
            return True

        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True

        return False

    def is_exact_subtree(self, t_supper, t_sub):
        if not t_supper and not t_sub:
            return True
        if not t_supper or not t_sub:
            return False

        return (
            t_supper.val == t_sub.val
            and self.is_exact_subtree(t_supper.left, t_sub.left)
            and self.is_exact_subtree(t_supper.right, t_sub.right)
        )


###############################################################
import unittest
from tree_utils import serialize, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertFalse(
            s.isSubtree(
                deserialize([10, 5, 20, 1, 7, None, 21]), deserialize([5, 1, 7, 1])
            )
        )
        self.assertTrue(
            s.isSubtree(
                deserialize([10, 5, 20, 1, 7, None, 21]), deserialize([5, 1, 7])
            )
        )
        self.assertTrue(
            s.isSubtree(
                deserialize([10, 5, 20, 1, 7, None, 21]), deserialize([20, None, 21])
            )
        )


if __name__ == "__main__":
    unittest.main()
