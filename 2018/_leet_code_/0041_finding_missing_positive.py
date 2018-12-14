class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        max_int = 0
        n = len(nums)
        if n == 0:
            return 1

        for i in range(n):
            if nums[i] <= 0 or nums[i] >= n:
                nums[i] = 0
            max_int = max(nums[i], max_int)

        for i in range(n):
            nums[nums[i] % n] += n

        for i in range(n):
            if nums[i] // n == 0:
                return i

        return n


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(4, s.firstMissingPositive([1, 2, 3]))
        self.assertEqual(4, s.firstMissingPositive([0, 1, 2, 3]))
        self.assertEqual(2, s.firstMissingPositive([1]))
        self.assertEqual(1, s.firstMissingPositive([0, 3]))
        self.assertEqual(3, s.firstMissingPositive([1, 2, 0]))
        self.assertEqual(2, s.firstMissingPositive([3, 4, -1, 1]))
        self.assertEqual(1, s.firstMissingPositive([7, 8, 9, 11, 12]))


if __name__ == "__main__":
    unittest.main()
