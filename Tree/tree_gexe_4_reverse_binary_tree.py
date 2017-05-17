#https://code.google.com/p/prep/wiki/ExercisesList

# Reverse a binary tree (left-right)

class TreeNode:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

def reverse(node):
    if not node:
        return

    reverse(node._left)
    reverse(node._right)

    swap = node._left
    node._left = node._right
    node._right = swap

    return node

def pre_order_iterative(node):
    visit = []
    stack = []
    stack.append(node)

    while len(stack) > 0:
        element = stack.pop()
        visit.append(element._value)
        if element._right: stack.append(element._right)
        if element._left: stack.append(element._left)
    return visit

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

        self.assertEqual([50, 40, 30, 45, 60, 55, 70], pre_order_iterative(root))
        root = reverse(root)
        self.assertEqual([50, 60, 70, 55, 40, 45, 30], pre_order_iterative(root))


    def test_missing_leaf(self):
        root = TreeNode(TreeNode(TreeNode(None, None, 30)
                               , None
                               , 40)
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)

        self.assertEqual([50, 40, 30, 60, 55, 70], pre_order_iterative(root))
        root = reverse(root)
        self.assertEqual([50, 60, 70, 55, 40, 30], pre_order_iterative(root))


    def test_missing_branch(self):
        root = TreeNode(None
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)

        self.assertEqual([50, 60, 55, 70], pre_order_iterative(root))
        root = reverse(root)
        self.assertEqual([50, 60, 70, 55], pre_order_iterative(root))
    

if __name__ == '__main__':
    unittest.main()