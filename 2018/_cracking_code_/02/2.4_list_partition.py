class Node:
    def __init__(self, value, next = None):
        self.next = next
        self.value = value


def partition(node, x):
    b_head = b_node = a_head = a_node = None

    while node:
        if node.value < x:
            if not b_head:
                b_head = b_node = node
            else:
                b_node.next = node
                b_node = b_node.next
        else:
            if not a_head:
                a_head = a_node = node
            else:
                a_node.next = node
                a_node = a_node.next
        node = node.next

    if a_node:
        a_node.next = None
    
    if not b_head:
        return a_head

    b_node.next = a_head
    return b_head

###############################################################
import unittest

def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx +1]
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
        n = [Node(1), Node(2), Node(3)]
        p = [Node(1), Node(9), Node(3)]
        
        print_ll(partition(from_list(n), 4))
        print_ll(partition(from_list(n), 0)) 
        print_ll(partition(from_list(p), 4))


if __name__ == '__main__':
    unittest.main()