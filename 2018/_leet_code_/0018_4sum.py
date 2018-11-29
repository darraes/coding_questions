class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        dedup = set()
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                l, r = j + 1, len(nums) - 1
                while l < r:
                    c_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if c_sum < target:
                        l += 1
                    elif c_sum > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                while j < len(nums) - 2 and nums[j] == nums[j + 1]:
                    j += 1
                j += 1
            while i < len(nums) - 3 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

    def fourSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        dedup = set()
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                l, r = j + 1, len(nums) - 1
                while l < r:
                    c_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if c_sum < target:
                        l += 1
                    elif c_sum > target:
                        r -= 1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                j += 1

            i += 1
        return list(res)


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            s.fourSum([1, 0, -1, 0, -2, 2], 0),
        )
        self.assertEqual([[-1, 0, 0, 1]], s.fourSum([1, 0, -1, 0], 0))
        self.assertEqual([], s.fourSum([1, 0, -1, 0], 1))
        self.assertEqual(
            [
                [-3, -2, 2, 3],
                [-3, -1, 1, 3],
                [-3, 0, 0, 3],
                [-3, 0, 1, 2],
                [-2, -1, 0, 3],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1],
            ],
            s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0),
        )


if __name__ == "__main__":
    unittest.main()
