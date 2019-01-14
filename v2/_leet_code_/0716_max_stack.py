class MaxStack:
    class Entry:
        def __init__(self, v, m):
            self.v = v
            self.m = m

    def __init__(self):
        self.store = []
        self.size = 0

    def push(self, v):
        m = v
        if self.size > 0:
            m = max(m, self.peekMax())

        self.size += 1
        self.store.append(MaxStack.Entry(v, m))

    def pop(self):
        self.size -= 1
        e = self.store.pop()
        return e.v

    def top(self):
        e = self.store[-1]
        return e.v

    def peekMax(self):
        return self.store[-1].m

    def popMax(self):
        m = self.store[-1].m
        buf = []

        for _ in range(self.size - 1, -1, -1):
            self.size -= 1
            if self.store[-1].v != m:
                buf.append(self.store.pop().v)
                continue
            del self.store[-1]
            break

        for v in reversed(buf):
            self.push(v)

        return m

    def print(self):
        print([(e.v, e.m) for e in self.store])


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        stack = MaxStack()
        stack.push(5)
        stack.push(1)
        stack.push(5)
        stack.print()
        self.assertEqual(5, stack.top())
        stack.print()
        self.assertEqual(5, stack.popMax())
        stack.print()
        self.assertEqual(1, stack.top())
        stack.print()
        self.assertEqual(5, stack.peekMax())
        self.assertEqual(1, stack.pop())
        self.assertEqual(5, stack.top())

    def test_2(self):
        stack = MaxStack()
        stack.push(5)
        stack.push(1)
        stack.print()
        self.assertEqual(5, stack.popMax())
        stack.print()
        self.assertEqual(1, stack.peekMax())


if __name__ == "__main__":
    unittest.main()



