class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self._max_coins([1] + nums + [1], {})
        return self._max_coins_2([1] + nums + [1], 0, len(nums) + 1, {})

    def _max_coins(self, nums, lookup):
        if len(nums) == 2:
            return 0

        key = ",".join([str(n) for n in nums])
        if key in lookup:
            return lookup[key]

        local_max = 0
        for i in range(1, len(nums) - 1):
            local_max = max(
                local_max,
                nums[i - 1] * nums[i] * nums[i + 1]
                + self._max_coins(nums[:i] + nums[i + 1 :], lookup),
            )
        lookup[key] = local_max
        return lookup[key]


    def _max_coins_2(self, nums, left, right, lookup):
        if left + 1 == right:
            return 0
        if (left, right) in lookup:
            return lookup[(left, right)]

        ans = 0
        for i in range(left + 1, right):
            ans = max(
                ans,
                nums[left] * nums[i] * nums[right]
                + self._max_coins_2(nums, left, i, lookup)
                + self._max_coins_2(nums, i, right, lookup),
            )
        lookup[(left, right)] = ans
        return ans


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(167, s.maxCoins([3, 1, 5, 8]))
        self.assertEqual(3, s.maxCoins([3]))
        self.assertEqual(16, s.maxCoins([3, 4]))


if __name__ == "__main__":
    unittest.main()
