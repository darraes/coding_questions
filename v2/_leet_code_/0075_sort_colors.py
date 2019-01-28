class Solution:
    def sortColors(self, nums):
        def swap(array, i, j):
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

        kRed = 0
        kWhite = 1
        kBlue = 2

        i = red_idx = 0
        blue_idx = len(nums) - 1

        while i <= blue_idx:
            if nums[i] < kWhite:
                swap(nums, red_idx, i)
                red_idx += 1
                i += 1
            elif nums[i] > kWhite:
                swap(nums, blue_idx, i)
                blue_idx -= 1
            else:
                i += 1


###############################################################
import unittest


def permute(nums):
    def _permute(nums, i):
        if i == len(nums):
            return [[]]

        current = nums[i]
        results = []

        sub_perms = _permute(nums, i + 1)
        for perm in sub_perms:
            for j in range(len(perm) + 1):
                results.append(perm[:j] + [current] + perm[j:])
        return results

    return _permute(nums, 0)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        nums = [2, 2, 0, 1, 1, 0]
        s.sortColors(nums)
        self.assertEqual([0, 0, 1, 1, 2, 2], nums)

        for nums in permute([2, 0, 2, 1, 1, 0]):
            s.sortColors(nums)
            self.assertEqual([0, 0, 1, 1, 2, 2], nums)


if __name__ == "__main__":
    unittest.main()
