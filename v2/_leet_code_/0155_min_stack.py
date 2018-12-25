class MinStack:
    class Item:
        def __init__(self, val, min_so_far):
            self.val = val
            self.min = min_so_far

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.store = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()
        self.store.append(
            MinStack.Item(x, min(x, cur_min) if cur_min is not None else x)
        )

    def pop(self):
        """
        :rtype: void
        """
        return self.store.pop().val

    def top(self):
        """
        :rtype: int
        """
        if len(self.store) == 0:
            return None
        return self.store[-1].val

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.store) == 0:
            return None
        return self.store[-1].min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(-3, minStack.getMin())
        minStack.pop()
        self.assertEqual(0, minStack.top())
        self.assertEqual(-2, minStack.getMin())


if __name__ == "__main__":
    unittest.main()