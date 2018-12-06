class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        idx = len(nums) - 1

        while idx > 0:
            if nums[idx] > nums[idx - 1]:
                # print(idx)
                min_so_far = 2 ** 64 - 1
                min_idx = -1

                s_idx = len(nums) - 1
                while s_idx >= idx:
                    val = nums[s_idx]
                    if val < min_so_far and val > nums[idx - 1]:
                        min_so_far = val
                        min_idx = s_idx
                        # print(min_so_far, min_idx)
                    s_idx -= 1
                
                # print(min_so_far, min_idx)
                # print(nums)
                tmp = nums[idx - 1]
                nums[idx - 1] = nums[min_idx]
                # print(nums)
                nums[min_idx] = tmp
                # print(nums)

                to_revert = nums[idx:]
                to_revert.reverse()
                nums[idx:] = to_revert
                # print(nums)
                return

            idx -= 1

        nums.reverse()




###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        test = [1, 2, 3]
        s.nextPermutation(test)
        self.assertEqual([1, 3, 2], test)

        test = [2, 1, 3]
        s.nextPermutation(test)
        self.assertEqual([2, 3, 1], test)

        test = [2, 3, 1]
        s.nextPermutation(test)
        self.assertEqual([3, 1, 2], test)

        test = [2, 3, 1, 1]
        s.nextPermutation(test)
        self.assertEqual([3, 1, 1, 2], test)

        test = [3, 2, 1]
        s.nextPermutation(test)
        self.assertEqual([1, 2, 3], test)

        test = [1, 1, 5]
        s.nextPermutation(test)
        self.assertEqual([1, 5, 1], test)

        test = [1, 5, 1]
        s.nextPermutation(test)
        self.assertEqual([5, 1, 1], test)

        test = [1, 2, 3, 6, 1, 3, 2]
        s.nextPermutation(test)
        self.assertEqual([1, 2, 3, 6, 2, 1, 3], test)

        test = [2,3,1,3,3]
        s.nextPermutation(test)
        self.assertEqual([2,3,3,1,3], test)


if __name__ == "__main__":
    unittest.main()
