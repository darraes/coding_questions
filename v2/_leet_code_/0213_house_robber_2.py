class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def _rob(s, e):
            nonlocal nums

            day_before = 0
            max_so_far = yesterday = nums[s]

            for i in range(s + 1, e + 1):
                max_so_far = max(yesterday, nums[i] + day_before)

                day_before = yesterday
                yesterday = max_so_far

            return max_so_far

        return max(_rob(1, len(nums) - 1), _rob(0, len(nums) - 2))


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(0, s.rob([]))
        self.assertEqual(5, s.rob([5]))
        self.assertEqual(5, s.rob([5, 1]))
        self.assertEqual(5, s.rob([1, 5]))
        self.assertEqual(3, s.rob([2, 3, 2]))
        self.assertEqual(4, s.rob([1, 2, 3, 1]))
        self.assertEqual(5, s.rob([1, 2, 3, 3]))


if __name__ == "__main__":
    unittest.main()
