class Solution:
    def pruneTree(self, root):
        def prune(node):
            if not node:
                return False

            if prune(node.left):
                node.left = None
            if prune(node.right):
                node.right = None

            if not node.left and not node.right and node.val == 0:
                return True
            return False

        if prune(root):
            return None
        return root


###############################################################
import unittest
from tree_utils import serialize, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            [1, None, 0, None, 1],
            serialize(s.pruneTree(deserialize([1, None, 0, 0, 1]))),
        )
        self.assertEqual(
            [1, 1, 0, 1, 1, None, 1],
            serialize(s.pruneTree(deserialize([1, 1, 0, 1, 1, 0, 1, 0]))),
        )


if __name__ == "__main__":
    unittest.main()
