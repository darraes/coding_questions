from bisect import bisect_left

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [(-1, -1, 2), (-1, 0, 1)], s.threeSum([-1, 0, 1, 2, -1, -4, -1, 0]))
        self.assertEqual(
            [(-1, 0, 1)], s.threeSum([-1, 0, 1]))
        self.assertEqual(
            [], s.threeSum([-2, 0, 1, 3, 4, 5]))
        self.assertEqual(
            [(-5, 0, 5), (-5, 1, 4)], s.threeSum([-5, 0, 1, 3, 4, 5]))
        self.assertEqual(
            [(0, 0, 0)], s.threeSum([0, 0, 0, 0]))


if __name__ == "__main__":
    unittest.main()