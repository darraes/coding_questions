from collections import deque
from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals


def next_node(node):
    def left_most(n):
        if not n:
            return None
        while n.left:
            n = n.left
        return n

    if not node.parent or node.right:
        return left_most(node.right)

    while node.parent and node == node.parent.right:
        node = node.parent

    if node:
        return node.parent

    return None


###############################################################
import unittest

def get_node(val, root):
    def _get_node(val, node):
        if not node:
            return False, None

        if node.value == val:
            return True, node

        on_left, n = _get_node(val, node.left)
        if on_left:
            return on_left, n

        on_right, n = _get_node(val, node.right)
        if on_right:
            return on_right, n

        return False, None
    _, n = _get_node(val, root)
    return n


class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build(
            [
                                   ["1"],
                        ["2",                   "3"],
                  ["4",       "5",        "6",        "7"],
                ["8", "9", "10", "11", "12", "13", "14", "15"],
            ]
        )
        self.assertEqual(12, next_node(get_node(1, root)).value)
        self.assertEqual(1, next_node(get_node(11, root)).value)
        self.assertEqual(2, next_node(get_node(9, root)).value)
        self.assertEqual(6, next_node(get_node(12, root)).value)
        self.assertEqual(3, next_node(get_node(13, root)).value)
        self.assertEqual(15, next_node(get_node(7, root)).value)
        self.assertEqual(7, next_node(get_node(14, root)).value)
        self.assertEqual(None, next_node(get_node(15, root)))


if __name__ == "__main__":
    unittest.main()
