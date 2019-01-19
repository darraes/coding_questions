class Solution:
    def connect(self, root):
        if not root:
            return

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


def print_ll(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node.val)
        buffer += " -> "
        node = node.next
    print(buffer)


def in_order(node):
    if not node:
        return

    in_order(node.left)
    print_ll(node)
    in_order(node.right)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        root = deserialize([-10, 9, 20, None, None, 15, 7])
        s.connect(root)
        in_order(root)

        root = deserialize([-10])
        s.connect(root)
        in_order(root)

        root = deserialize([-10, 9, 8])
        s.connect(root)
        in_order(root)

        root = deserialize([-10, 9])
        s.connect(root)
        in_order(root)


if __name__ == "__main__":
    unittest.main()
