# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.

from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counters = defaultdict(int)
        for num in nums:
            counters[num] += 1

        store = []
        for num, v in counters.items():
            heappush(store, (v, num))
            if len(store) > k:
                heappop(store)

        return [num for k, num in reversed(store)]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([1, 2], s.topKFrequent([1, 1, 1, 2, 2, 3], 2))


if __name__ == "__main__":
    unittest.main()
