# http://www.careercup.com/question?id=5344154741637120
# 
# Sink Zero in Binary Tree. Swap zero value of a node with non-zero value of
# one of its descendants so that no node with value zero could be parent of
# node with non-zero.

from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals


def _swap(src_node, dst_node):
    tmp = src_node._value
    src_node._value = dst_node._value
    dst_node._value = tmp


def _sink(node):
    if not node or node._value != 0:
        return
    
    if node._right and node._right._value != 0:
        # print "right swap ", node._value, ", ", node._right._value
        _swap(node, node._right)
        _sink(node._right)
    elif node._left and node._left._value != 0:
        # print "left swap ", node._value, ", ", node._left._value
        _swap(node, node._left)
        _sink(node._left)


def sink_zeros(node):
    if not node:
        return

    sink_zeros(node._left)
    sink_zeros(node._right)

    if node._value == 0:
        _sink(node)


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build([["1"],
                               ["2", "0"],
                               ["0", "5", "6", "7"],
                               ["8", "9", "0", "11", "8", "9", "0", "1"]])
        expt = friendly_build([["1"],
                               ["2", "7"],
                               ["9", "5", "6", "1"],
                               ["8", "0", "0", "11", "8", "9", "0", "0"]])
        sink_zeros(root)
        pretty_print(root)
        self.assertTrue(tree_equals(expt, root))

    def test_2(self):
        root = friendly_build([["1"],
                               ["0", "0"],
                               ["0", "0", "0", "7"],
                               ["8", "0", "0", "0", "0", "0", "0", "1"]])
        expt = friendly_build([["1"],
                               ["8", "7"],
                               ["0", "0", "0", "1"],
                               ["0", "0", "0", "0", "0", "0", "0", "0"]])
        sink_zeros(root)
        pretty_print(root)
        self.assertTrue(tree_equals(expt, root))

    def test_3(self):
        root = friendly_build([["0"],
                               ["0", "0"],
                               ["0", "0", "0", "0"],
                               ["0", "0", "0", "0", "0", "0", "0", "1"]])
        expt = friendly_build([["1"],
                               ["0", "0"],
                               ["0", "0", "0", "0"],
                               ["0", "0", "0", "0", "0", "0", "0", "0"]])
        sink_zeros(root)
        pretty_print(root)
        self.assertTrue(tree_equals(expt, root))


if __name__ == '__main__':
    unittest.main()