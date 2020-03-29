class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], idx]
            complements[num] = idx

        return []


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 7, 11, 15], 18))
print(s.twoSum([2, 7, 11, 15], 26))
print(s.twoSum([2, 7, 11, 15], 17))
print(s.twoSum([3, 3], 6))