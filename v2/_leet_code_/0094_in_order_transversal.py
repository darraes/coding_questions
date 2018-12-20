# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        node = root
        ans = []
        while node or len(stack) > 0:
            if node:
                stack.append(node)
                node = node.left
            else:
                visit = stack.pop()
                ans.append(visit.val)
                node = visit.right
        return ans


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

    return _build(array)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([1, 3, 2], s.inorderTraversal(build([1, None, 2, 3])))
        self.assertEqual([1], s.inorderTraversal(build([1])))
        self.assertEqual([2, 1, 3], s.inorderTraversal(build([1, 2, None, None, 3])))


if __name__ == "__main__":
    unittest.main()
