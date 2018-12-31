# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def _rob(node, can_rob, cache):
            if not node:
                return 0

            if (node, can_rob) in cache:
                return cache[(node, can_rob)]

            ans = 0
            if can_rob:
                ans = max(
                    node.val
                    + _rob(node.left, False, cache)
                    + _rob(node.right, False, cache),
                    _rob(node.left, True, cache) + _rob(node.right, True, cache),
                )
            else:
                ans = _rob(node.left, True, cache) + _rob(node.right, True, cache)

            cache[(node, can_rob)] = ans
            return ans

        return _rob(root, True, {})


###############################################################
import unittest
from tree_utils import pretty_print, serialize, deserialize, tree_equals


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        problem = [3, 2, 3, None, 3, None, 1]
        self.assertEqual(7, s.rob(deserialize(problem)))

        problem = [3, 4, 5, 1, 3, None, 1]
        self.assertEqual(9, s.rob(deserialize(problem)))


if __name__ == "__main__":
    unittest.main()
