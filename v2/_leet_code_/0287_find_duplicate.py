class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        i = nums[0]
        while slow != i:
            slow = nums[slow]
            i = nums[i]

        return i

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(2, s.findDuplicate([1,3,4,2,2]))
        self.assertEqual(3, s.findDuplicate([3,1,3,4,2]))
        self.assertEqual(2, s.findDuplicate([2, 2, 2]))



if __name__ == "__main__":
    unittest.main()