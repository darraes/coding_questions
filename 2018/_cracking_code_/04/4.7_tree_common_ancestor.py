# Cracking the Code Interview - 4.7
# Find the common ancestor of 2 nodes without having a pointer to the parent
# node

from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals

class State:
    def __init__(self):
        self.common_ancestor = None
        self.found_p = False
        self.found_q = False

    def merge(self, state):
        if state.found_p:
            self.found_p = True
        if state.found_q:
            self.found_q = True
        if state.common_ancestor:
            self.common_ancestor = state.common_ancestor

    def maybe_mark_ancestor(self, node):
        if self.found_p and self.found_q and not self.common_ancestor:
            self.common_ancestor = node


def find_ancestor(root, p, q):
    if not root:
        return State()

    result = State()

    if root._value == p._value:
        result.found_p = True
    if root._value == q._value:
        result.found_q = True


    l_state = find_ancestor(root._left, p, q)
    r_state = find_ancestor(root._right, p, q)

    result.merge(l_state)
    result.merge(r_state)

    result.maybe_mark_ancestor(root)

    return result


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build([["1"],
                               ["2", "3"],
                               ["4", "5", "6", "7"],
                               ["8", "9", "10", "11", "12", "13", "14", "15"]])
        pretty_print(root)
        state = find_ancestor(root, 
                              TreeNode(None, None, 8),
                              TreeNode(None, None, 10))
        self.assertEquals(2, state.common_ancestor._value)

        state = find_ancestor(root, 
                              TreeNode(None, None, 2),
                              TreeNode(None, None, 10))
        self.assertEquals(2, state.common_ancestor._value)

        state = find_ancestor(root, 
                              TreeNode(None, None, 1),
                              TreeNode(None, None, 10))
        self.assertEquals(1, state.common_ancestor._value)

        state = find_ancestor(root, 
                              TreeNode(None, None, 8),
                              TreeNode(None, None, 15))
        self.assertEquals(1, state.common_ancestor._value)

        state = find_ancestor(root, 
                              TreeNode(None, None, 8),
                              TreeNode(None, None, 3))
        self.assertEquals(1, state.common_ancestor._value)


if __name__ == '__main__':
    unittest.main()