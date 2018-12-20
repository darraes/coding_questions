class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


def remove(node):
    if not node.next:
        raise "Not Possible"

    node.value = node.next.value
    node.next = node.next.next


###############################################################
import unittest


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx + 1]
        idx += 1
    return list[0]


def print_ll(head):
    buffer = ""
    node = head
    while node:
        buffer += str(node.value)
        buffer += " -> "
        node = node.next
    print(buffer)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("===================")
        source = [Node(1), Node(2), Node(3), Node(5), Node(7)]
        n = from_list(source)
        print_ll(n)
        remove(source[1])
        print_ll(n)


if __name__ == "__main__":
    unittest.main()
