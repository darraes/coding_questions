class Queue:
    def __init__(self, capacity=3):
        self.size = 0
        self.capacity = capacity

        self.storage = [None] * capacity
        self.nidx = 0
        self.fidx = 0

    def enqueue(self, v):
        if self.size == self.capacity:
            return False

        self.storage[self.nidx] = v
        self.nidx = (self.nidx + 1) % self.capacity
        self.size += 1

        return True

    def dequeue(self):
        if self.size == 0:
            raise "Full"

        res = self.storage[self.fidx]
        self.fidx = (self.fidx + 1) % self.capacity
        self.size -= 1

        return res


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        q = Queue()
        self.assertTrue(q.enqueue(1))
        self.assertTrue(q.enqueue(2))
        self.assertTrue(q.enqueue(3))
        self.assertFalse(q.enqueue(4))
        self.assertEqual(1, q.dequeue())
        self.assertTrue(q.enqueue(4))
        self.assertFalse(q.enqueue(5))
        self.assertEqual(2, q.dequeue())
        self.assertEqual(3, q.dequeue())
        self.assertTrue(q.enqueue(5))
        self.assertTrue(q.enqueue(6))
        self.assertEqual(4, q.dequeue())
        self.assertEqual(5, q.dequeue())
        self.assertEqual(6, q.dequeue())



if __name__ == "__main__":
    unittest.main()
