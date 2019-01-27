from collections import deque
from tree_utils import TreeNode, pretty_print, friendly_build, tree_equals


def is_bst(root):
    stack = []
    last = None
    node = root

    while node or len(stack) > 0:
        if node:
            stack.append(node)
            node = node.left
        else:
            visiting = stack.pop()
            if last and visiting.value < last:
                return False
            last = visiting.value
            node = visiting.right
    return True


###############################################################
import unittest


def print_lists(lists):
    for l in lists:
        print([n.value for n in l])


class TestFunctions(unittest.TestCase):
    def test_1(self):
        root = friendly_build(
            [
                ["1"],
                ["2", "3"],
                ["4", "5", "6", "7"],
                ["8", "9", "10", "11", "12", "13", "14", "15"],
            ]
        )
        self.assertFalse(is_bst(root))

        root = friendly_build(
            [["10"], ["5", "15"], ["4", "6", "12", "17"]]
        )
        self.assertTrue(is_bst(root))


if __name__ == "__main__":
    unittest.main()
