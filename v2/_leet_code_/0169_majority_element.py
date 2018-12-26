from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
            if counter[n] > len(nums) // 2:
                return n
        return -1