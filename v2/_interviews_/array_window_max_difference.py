# Given an integer array and a window size, calculate the max different
# between the integer of all windows
#
# ### ====== requires Python 3
from collections import deque

from collections import deque


class MQueue(object):
    class Element:
        def __init__(self, val, ignored):
            self.val = val
            self.ignored = ignored

    def __init__(self, compare):
        self.store = deque()
        self.compare = compare

    def enqueue(self, val):
        count = 0
        while len(self.store) > 0 and self.compare(self.store[-1].val, val):
            count += 1 + self.store[-1].ignored
            self.store.pop()
        self.store.append(MQueue.Element(val, count))

    def next(self):
        if len(self.store) > 0:
            return self.store[0].val
        return None

    def dequeue(self):
        if len(self.store) > 0:
            if self.store[0].ignored > 0:
                self.store[0].ignored -= 1
            else:
                self.store.popleft()


def compute_max_distance(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    ans = []
    if k == 0 or len(nums) == 0:
        return []

    max_queue = MQueue(lambda o, n: n > o)
    min_queue = MQueue(lambda o, n: n < o)
    for i in range(len(nums)):
        if i < k - 1:
            max_queue.enqueue(nums[i])
            min_queue.enqueue(nums[i])
            continue

        max_queue.enqueue(nums[i])
        min_queue.enqueue(nums[i])

        ans.append(max_queue.next() - min_queue.next())
        
        max_queue.dequeue()
        min_queue.dequeue()

    return max(ans)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        distance = compute_max_distance([1, 14, 12, 17, 8, 9, 45, 12, 16, 8], 5)
        self.assertEqual(37, distance)

        distance = compute_max_distance([2, 1, 1, 1, 1, 3, 1, 2, 1, 1], 5)
        self.assertEqual(2, distance)


if __name__ == "__main__":
    unittest.main()
