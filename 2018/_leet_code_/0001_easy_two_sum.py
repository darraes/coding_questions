# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = [(idx, num)for idx, num in enumerate(nums)]

        index.sort(key= lambda elem: elem[1])
        start = 0
        end = len(index) - 1

        while (start <= end):
            cur_sum = index[start][1] + index[end][1]
            if cur_sum == target:
                break
            elif cur_sum < target:
                start += 1
            else:
                end -= 1

        return [index[start][0], index[end][0]]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 7, 11, 15], 26))
print(s.twoSum([2, 7, 11, 15], 17))
print(s.twoSum([3, 3], 6))