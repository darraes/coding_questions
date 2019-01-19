# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        parents = [root]
        children = []

        while parents:
            prev = None
            for p in parents:
                if p.left:
                    children.append(p.left)
                if p.right:
                    children.append(p.right)
                if prev:
                    prev.next = p
                prev = p

            parents = children
            children = []


###############################################################
import unittest
from tree_utils import pretty_print, serialize, deserialize, tree_equals


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        problem = [-10, 9, 20, None, None, 15, 7]
        s.connect(deserialize(problem))

        problem = [-10]
        s.connect(deserialize(problem))

        problem = [-10, 9, 8]
        s.connect(deserialize(problem))

        problem = [-10, 9]
        s.connect(deserialize(problem))


if __name__ == "__main__":
    unittest.main()
