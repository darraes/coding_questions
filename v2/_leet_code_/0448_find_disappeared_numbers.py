class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            idx = abs(nums[i - 1])
            nums[idx - 1] = -1 * abs(nums[idx - 1]) 

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([5,6], s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        self.assertEqual([5,6], s.findDisappearedNumbers([4,3,2,7,2,3,1]))
        self.assertEqual([], s.findDisappearedNumbers([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    unittest.main()
