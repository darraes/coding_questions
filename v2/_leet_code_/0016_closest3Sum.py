class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = 2 ** 64 - 1
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                distance = s - target
                if abs(distance) < abs(closest - target):
                    closest = s
                if distance < 0:
                    l += 1
                elif distance > 0:
                    r -= 1
                else:
                    return target
        return closest


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1, -4], 1))
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1], 100))
        self.assertEqual(2, s.threeSumClosest([-1, 2, 1], -100))
        self.assertEqual(-1, s.threeSumClosest([-4, -1, 1, 2], 0))
        self.assertEqual(-3, s.threeSumClosest([-4, -1, 1, 2], -3))
        self.assertEqual(10, s.threeSumClosest([-4, -1, 1, 2, 7, -12, 2345], 10))
        self.assertEqual(-23, s.threeSumClosest([-4, -1, 1, 2, 7, -29, 2345], -22))
        self.assertEqual(2346, s.threeSumClosest([-4, -1, 1, 2, 7, -29, 2340], 2345))


if __name__ == "__main__":
    unittest.main()
