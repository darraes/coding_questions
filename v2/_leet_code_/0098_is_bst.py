# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.inorderTraversal(root)

    def inorderTraversal(self, node):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        last_visited =  -2 ** 64 - 1
        while node or len(stack) > 0:
            if node:
                stack.append(node)
                node = node.left
            else:
                visit = stack.pop()
                if last_visited >= visit.val:
                    return False
                last_visited = visit.val
                node = visit.right
        return True


###############################################################
import unittest

def build(array):
    idx = 0

    def _build(array):
        nonlocal idx
        node = None
        if idx < len(array) and array[idx] is not None:
            node = TreeNode(array[idx])
            idx += 1
            node.left = _build(array)
            node.right = _build(array)
            return node
        else:
            idx += 1
            return None

    root =  _build(array)
    return root



class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(True, s.isValidBST(build([2, 1, None, None, 3])))
        self.assertEqual(False, s.isValidBST(build([5, 1, 4, None, None, 3, 6])))


if __name__ == "__main__":
    unittest.main()