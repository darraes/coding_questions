class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


def is_palindrome(n):
    stack = []

    cur = n
    while cur:
        stack.append(cur)
        cur = cur.next

    while stack:
        p = stack.pop()
        if n.val != p.val:
            return False

        n = n.next

    return True

def is_palindrome_2(n):
    slow = fast = n
    stack = []

    while fast and fast.next:
        stack.append(slow)
        slow = slow.next
        fast = fast.next.next

    right = None
    if not fast:
        right = slow
    elif not fast.next:
        right = slow.next

    while stack:
        if right.val != stack[-1].val:
            return False
        stack.pop()
        right = right.next

    return True




##################################################
import unittest


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx + 1]
        idx += 1
    return list[0]


class TestFunctions(unittest.TestCase):
    def test_positive(self):
        head = from_list(
            [
                Node(1),
                Node(2),
                Node(3),
                Node(3),
                Node(2),
                Node(1),
            ]
        )
        self.assertTrue(is_palindrome(head))

        head = from_list(
            [Node(1), Node(2), Node(3), Node(2), Node(1)]
        )
        self.assertTrue(is_palindrome(head))

        head = from_list([Node(1), Node(2), Node(2), Node(1)])
        self.assertTrue(is_palindrome(head))

        head = from_list([Node(1), Node(2), Node(1)])
        self.assertTrue(is_palindrome(head))

        head = from_list([Node(1), Node(1)])
        self.assertTrue(is_palindrome(head))

        head = from_list([Node(1)])
        self.assertTrue(is_palindrome(head))

    def test_negative(self):
        head = from_list(
            [
                Node(1),
                Node(2),
                Node(3),
                Node(3),
                Node(4),
                Node(2),
                Node(1),
            ]
        )
        self.assertFalse(is_palindrome(head))

        head = from_list(
            [
                Node(1),
                Node(2),
                Node(3),
                Node(2),
                Node(4),
                Node(1),
            ]
        )
        self.assertFalse(is_palindrome(head))

        head = from_list(
            [Node(1), Node(4), Node(2), Node(2), Node(1)]
        )
        self.assertFalse(is_palindrome(head))

        head = from_list([Node(1), Node(2), Node(1), Node(4)])
        self.assertFalse(is_palindrome(head))

        head = from_list([Node(4), Node(1), Node(1)])
        self.assertFalse(is_palindrome(head))

        head = from_list([Node(1), Node(4)])
        self.assertFalse(is_palindrome(head))

    def test_positive2(self):
        head = from_list(
            [
                Node(1),
                Node(2),
                Node(3),
                Node(3),
                Node(2),
                Node(1),
            ]
        )
        self.assertTrue(is_palindrome_2(head))

        head = from_list(
            [Node(1), Node(2), Node(3), Node(2), Node(1)]
        )
        self.assertTrue(is_palindrome_2(head))

        head = from_list([Node(1), Node(2), Node(2), Node(1)])
        self.assertTrue(is_palindrome_2(head))

        head = from_list([Node(1), Node(2), Node(1)])
        self.assertTrue(is_palindrome_2(head))

        head = from_list([Node(1), Node(1)])
        self.assertTrue(is_palindrome_2(head))

        head = from_list([Node(1)])
        self.assertTrue(is_palindrome_2(head))

    def test_negative2(self):
        head = from_list(
            [
                Node(1),
                Node(2),
                Node(3),
                Node(3),
                Node(4),
                Node(2),
                Node(1),
            ]
        )
        self.assertFalse(is_palindrome_2(head))

        head = from_list(
            [
                Node(1),
                Node(2),
                Node(3),
                Node(2),
                Node(4),
                Node(1),
            ]
        )
        self.assertFalse(is_palindrome_2(head))

        head = from_list(
            [Node(1), Node(4), Node(2), Node(2), Node(1)]
        )
        self.assertFalse(is_palindrome_2(head))

        head = from_list([Node(1), Node(2), Node(1), Node(4)])
        self.assertFalse(is_palindrome_2(head))

        head = from_list([Node(4), Node(1), Node(1)])
        self.assertFalse(is_palindrome_2(head))

        head = from_list([Node(1), Node(4)])
        self.assertFalse(is_palindrome_2(head))


if __name__ == "__main__":
    unittest.main()
