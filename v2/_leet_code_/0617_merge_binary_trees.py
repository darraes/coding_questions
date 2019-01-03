# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def merge(n1, n2):
            if not n1:
                return n2
            if not n2:
                return n1

            n1.val += n2.val

            n1.left = merge(n1.left, n2.left)
            n1.right = merge(n1.right, n2.right)
            return n1

        return merge(t1, t2)


###############################################################
import unittest
from tree_utils import serialize, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            [3, 4, 5, 5, 4, None, 7],
            serialize(
                s.mergeTrees(
                    deserialize([1, 3, 2, 5]), deserialize([2, 1, 3, None, 4, None, 7])
                )
            ),
        )

        self.assertEqual(
            [3],
            serialize(
                s.mergeTrees(
                    deserialize([3]), deserialize([])
                )
            ),
        )
        self.assertEqual(
            [3],
            serialize(
                s.mergeTrees(
                    deserialize([]), deserialize([3])
                )
            ),
        )


if __name__ == "__main__":
    unittest.main()
