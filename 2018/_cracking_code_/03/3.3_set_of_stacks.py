class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if not self.top:
            return None

        value = self.top.value
        self.top = self.top.next
        self.size -= 1

        return value

    def peek(self):
        if not self.top:
            return None

        value = self.top.value
        return value

    def empty(self):
        return self.size == 0

class SetOfStacks:
    MAX_SIZE = 3

    def __init__(self):
        self.stacks = [Stack()]
        self.idx = 0

    def push(self, value):
        if self.stacks[self.idx].size >= SetOfStacks.MAX_SIZE:
            print("Stack roll over", self.idx)
            self.stacks.append(Stack())
            self.idx += 1

        self.stacks[self.idx].push(value)

    def pop(self):
        res = self.stacks[self.idx].pop()
        if self.idx > 0 and self.stacks[self.idx].empty():
            print("Stack roll back", self.idx)
            del self.stacks[self.idx]
            self.idx -= 1
        return res

###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = SetOfStacks()
        s.push(0)
        s.push(10)
        s.push(100)

        self.assertEqual(100, s.pop())
        self.assertEqual(10, s.pop())
        self.assertEqual(0, s.pop())

        s.push(0)
        s.push(10)
        s.push(100)
        s.push(1)
        s.push(11)
        s.push(101)

        self.assertEqual(101, s.pop())
        self.assertEqual(11, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(100, s.pop())
        self.assertEqual(10, s.pop())
        self.assertEqual(0, s.pop())

        s.push(0)
        s.push(10)
        s.push(100)
        s.push(1)
        s.push(11)
        s.push(101)
        s.push(2)
        s.push(12)
        s.push(102)

        self.assertEqual(102, s.pop())
        self.assertEqual(12, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(101, s.pop())
        self.assertEqual(11, s.pop())
        self.assertEqual(1, s.pop())
        self.assertEqual(100, s.pop())
        self.assertEqual(10, s.pop())
        self.assertEqual(0, s.pop())


if __name__ == '__main__':
    unittest.main()