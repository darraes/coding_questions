class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self._max_sub_array(nums, 0, len(nums) - 1)

    def _max_sub_array(self, nums, left, right):
        if left > right:
            return -2 ** 64
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        return max(
            self._max_to_the_left(nums, mid, left)
            + nums[mid]
            + self._max_to_the_right(nums, mid, right),
            self._max_sub_array(nums, left, mid - 1),
            self._max_sub_array(nums, mid + 1, right),
        )

    def _max_to_the_left(self, nums, mid, left):
        i = mid - 1
        max_sum = current_sum = 0

        while i >= left:
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            i -= 1

        return max_sum

    def _max_to_the_right(self, nums, mid, right):
        i = mid + 1
        max_sum = current_sum = 0

        while i <= right:
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            i += 1

        return max_sum


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(6, s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(11, s.maxSubArray([9, -2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(4, s.maxSubArray([4]))
        self.assertEqual(-2, s.maxSubArray([-2]))


if __name__ == "__main__":
    unittest.main()
