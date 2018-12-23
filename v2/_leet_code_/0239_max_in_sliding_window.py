from collections import deque


class MQueue(object):
    class Element:
        def __init__(self, val, tail_count):
            self.val = val
            self.tail_count = tail_count

    def __init__(self):
        self.store = deque()

    def enqueue(self, val):
        count = 0
        while len(self.store) > 0 and self.store[-1].val < val:
            count += 1 + self.store[-1].tail_count
            self.store.pop()
        self.store.append(MQueue.Element(val, count))

    def max(self):
        if len(self.store) > 0:
            return self.store[0].val
        return None

    def dequeue(self):
        if len(self.store) > 0:
            if self.store[0].tail_count > 0:
                self.store[0].tail_count -= 1
            else:
                self.store.popleft()


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        queue = MQueue()
        for i in range(len(nums)):
            if i < k - 1:
                queue.enqueue(nums[i])
                continue

            queue.enqueue(nums[i])
            ans.append(queue.max())
            queue.dequeue()

        return ans


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [3, 3, 5, 5, 6, 7], s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
        )


if __name__ == "__main__":
    unittest.main()
