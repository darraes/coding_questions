from collections import deque

class BiNode:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


def friendly_build(lines):
    def build_node(value):
        if value == "N":
            return None
        return BiNode(None, None, int(value))

    parents = deque()
    next = deque()
    next.append(build_node(lines[0][0]))
    root = None

    for i in range(len(lines)):
        j = 0
        while len(parents) > 0:
            current_parent = parents.popleft()
            if root is None:
                root = current_parent

            current_parent.left = build_node(lines[i][j])
            j += 1
            current_parent.right = build_node(lines[i][j])
            j += 1

            if current_parent.left:
                next.append(current_parent.left)
            if current_parent.right:
                next.append(current_parent.right)

        if i != 0 and j != len(lines[i]):
            raise

        parents = next
        next = deque()

    return root


def convert(tree):
    head = current = None

    def visit(node):
        nonlocal head, current
        if not node:
            return

        visit(node.left)

        if not current:
            head = current = node
        else:
            current.right = node
            node.left = current
            current = current.right

        visit(node.right)
    visit(tree)
    return head


def listify(node):
    parents = [node]
    children = []
    tail = None

    while parents:
        for i, p in enumerate(parents):
            if p.left:
                children.append(p.left)
            if p.right:
                children.append(p.right)

            p.left = None
            p.right = None
            if i < len(parents) - 1:
                p.right = parents[i + 1]
            if i > 0:
                p.left = parents[i - 1]

        if tail:
            tail.right = parents[0]
            parents[0].left = tail

        tail = parents[-1]
        parents = children
        children = []

    return node



###############################################################
import unittest


def print_ll(head):
    buffer = ""
    node = head
    last = None
    while node:
        last = node
        buffer += str(node.val)
        buffer += " -> "
        node = node.right
    print(buffer)

    buffer = ""
    while last:
        buffer += str(last.val)
        buffer += " -> "
        last = last.left
    print(buffer)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        tree = friendly_build([[10], [3, 15], [1, 4, 12, 16]])
        head = convert(tree)
        print_ll(head)

        tree = friendly_build([[10], [3, 15], [1, 4, 12, 16]])
        head = listify(tree)
        print_ll(head)


if __name__ == "__main__":
    unittest.main()
