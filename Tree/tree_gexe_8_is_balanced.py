# https://code.google.com/p/prep/wiki/ExercisesList

# Tell if a binary tree is balanced

class TreeNode:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right


def is_balanced(node, factor):
    if not node:
        return True, 0

    is_right, h_right = is_balanced(node._right, factor)
    if not is_right:
        return False, -1

    is_left, h_left = is_balanced(node._left, factor)
    if not is_left:
        return False, -1

    unbalance = abs(h_right - h_left) < factor
    return unbalance, max(h_right, h_left) + 1


###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_full_tree(self):
        root = TreeNode(TreeNode(TreeNode(None, None, 30)
                               , TreeNode(None, None, 45)
                               , 40)
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)

        self.assertEqual((True, 3), is_balanced(root, 2))

    def test_left_unbalanced(self):
        root = TreeNode(None
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)

        self.assertEqual((False, 3), is_balanced(root, 2))
    

if __name__ == '__main__':
    unittest.main()