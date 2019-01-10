from collections import deque

class MovingAverage:

    def __init__(self, size):
        self.capacity = size
        self.size = 0
        self.sum = 0
        self.window = deque()
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.append(val)
        self.size += 1
        self.sum += val

        if self.size > self.capacity:
            self.sum -= self.window.popleft()
            self.size -= 1

        return self.sum / self.size

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)



###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        m = MovingAverage(3)

        self.assertEqual(1.0, m.next(1))
        self.assertEqual(5.5, m.next(10))
        self.assertEqual(4.666666666666667, m.next(3))
        self.assertEqual(6.0, m.next(5))


if __name__ == "__main__":
    unittest.main()