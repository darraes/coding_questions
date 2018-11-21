class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.min = None

class Stack:
    def __init__(self):
        self.top = None
        self.last_min = None

    def push(self, value):
        if not self.last_min or value < self.last_min:
            self.last_min = value

        node = Node(value)
        node.min = self.last_min
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None

        value = self.top.value
        self.top = self.top.next

        return value

    def peek(self):
        if not self.top:
            return None

        value = self.top.value
        return value

    def min(self):
        if not self.top:
            return None
        return self.top.min


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Stack()
        self.assertEqual(None, s.pop())
        self.assertEqual(None, s.peek())
        self.assertEqual(None, s.min())

        s.push(10)
        self.assertEqual(10, s.peek())
        self.assertEqual(10, s.min())

        s.push(20)
        self.assertEqual(20, s.peek())
        self.assertEqual(10, s.min())

        s.push(5)
        self.assertEqual(5, s.peek())
        self.assertEqual(5, s.min())

        s.push(7)
        self.assertEqual(7, s.peek())
        self.assertEqual(5, s.min())


if __name__ == '__main__':
    unittest.main()