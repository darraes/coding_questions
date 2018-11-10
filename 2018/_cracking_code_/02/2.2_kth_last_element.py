# Cracking the code interview - 2.5

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __len__(self):
        if self.next is None:
            return 1
        return 1 + len(self.next)

    def __eq__(self, that):
        return self.value == that.value


def kth_last_element(head, k):
    slow = fast = head

    for i in range(k):
        if not fast.next:
            return None

        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


###############################################################
import unittest


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx +1]
        idx += 1 
    return list[0]


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("===================")
        l1 = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)]
        
        self.assertEqual(Node(4), kth_last_element(from_list(l1), 4))


if __name__ == '__main__':
    unittest.main()









