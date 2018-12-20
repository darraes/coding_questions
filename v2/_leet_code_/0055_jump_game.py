class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = cur_end = farthest = 0
        while i < len(nums):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                if farthest >= len(nums) - 1:
                    return True
                if cur_end == farthest:
                    return False
                cur_end = farthest
            i += 1
        return True


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(True, s.canJump([2, 3, 0, 1, 4]))
        self.assertEqual(False, s.canJump([2, 0, 0, 0, 0]))
        self.assertEqual(False, s.canJump([0, 0, 0, 0, 0]))
        self.assertEqual(False, s.canJump([3, 2, 1, 0, 4]))
        self.assertEqual(True, s.canJump([2, 3, 1, 1, 4]))
        self.assertEqual(True, s.canJump([1, 1, 1, 1, 1, 1]))
        self.assertEqual(True, s.canJump([4, 1, 1, 1, 1, 1]))
        self.assertEqual(True, s.canJump([3, 1, 3, 1, 1, 1]))
        self.assertEqual(True, s.canJump([3]))
        self.assertEqual(True, s.canJump([0]))

if __name__ == "__main__":
    unittest.main()