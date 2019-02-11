# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "{}".format(self.val)


class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.flat_node(root)

    def flat_node(self, node):
        if not node:
            return (None, None)

        left = node.left
        right = node.right
        l_head, l_tail = self.flat_node(left)
        r_head, r_tail = self.flat_node(right)

        tail = node
        if l_head:
            tail.right = l_head
            tail = l_tail if l_tail else l_head

        if r_head:
            tail.right = r_head
            tail = r_tail if r_tail else r_head

        node.left = None
        return node, tail


###############################################################
import unittest


def pre_order(node):
    if node is None:
        return

    print(node.val)
    pre_order(node.left)
    pre_order(node.right)


def print_ll(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node.val)
        buffer += " -> "
        node = node.right
    print(buffer)


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

    root = _build(array)
    return root


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        root = build([1, 2, 3, None, None, 4, None, None, 5, None, 6, None, None])
        ll, tail = s.flat_node(root)
        print_ll(ll)

        root = build([1])
        ll, tail = s.flat_node(root)
        print_ll(ll)

        root = build([])
        ll, tail = s.flat_node(root)
        print_ll(ll)


if __name__ == "__main__":
    unittest.main()
