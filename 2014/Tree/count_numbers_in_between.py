# http://www.careercup.com/question?id=5165570324430848

# Given a Binary Search tree of integers, you need to return the number of 
# nodes having values between two given integers. You can assume that you 
# already have some extra information at each node 
# (number of children in left and right subtrees !!).

class TreeNode:
    def __init__(self, left, right, value):
        self._left = left
        self._right = right
        self._value = value

def count_nodes_between(root, low, up):
    if root is None: return 0

    if root._value < low: return count_nodes_between(root._right, low, up)
    if root._value > up: return count_nodes_between(root._left, low, up)
    else:
        return 1 + count_nodes_between(root._right, low, up) \
                 + count_nodes_between(root._left, low, up)


###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_basic(self):
        root = TreeNode(TreeNode(TreeNode(None, None, 30)
                               , TreeNode(None, None, 45)
                               , 40)
                      , TreeNode(TreeNode(None, None, 55)
                               , TreeNode(None, None, 70)
                               , 60)
                      , 50)

        self.assertEqual(4, count_nodes_between(root, 30, 50))
        self.assertEqual(2, count_nodes_between(root, 31, 49))
        self.assertEqual(7, count_nodes_between(root, 1, 100))
        self.assertEqual(1, count_nodes_between(root, 39, 41))


if __name__ == '__main__':
    unittest.main()
