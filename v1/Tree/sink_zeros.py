# http://www.careercup.com/question?id=5344154741637120
# 
# Sink Zero in Binary Tree. Swap zero value of a node with non-zero value of
# one of its descendants so that no node with value zero could be parent of
# node with non-zero.

from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals

def sink_node(node):
    while True:
        if not node or (not node._left and not node._right):
             return
        
        c = node._left if node._left and not node._right \
            else (node._right if node._right and not node._left
                  else (node._right if node._right._value > node._left._value 
                        else node._left)
                  )

        # Swap values
        tmp = c._value
        c._value = node._value
        node._value = tmp
        
        # Move down
        node = c

def sink_zeros(node):
    if not node: 
        return
        
    sink_zeros(node._left)
    sink_zeros(node._right)

    if node._value == 0:
        sink_node(node)


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_basic(self):
        root = friendly_build([["1"],
                               ["2", "0"],
                               ["0", "5", "6", "7"],
                               ["8", "9", "0", "11", "8", "9", "0", "1"]])
        expt = friendly_build([["1"],
                               ["2", "7"],
                               ["9", "5", "6", "1"],
                               ["8", "0", "0", "11", "8", "9", "0", "0"]])
        sink_zeros(root)
        self.assertTrue(tree_equals(expt, root))


if __name__ == '__main__':
    unittest.main()