class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        c = p = 1
        while p < len(nums):
            if nums[p] != nums[c - 1]:
                nums[c] = nums[p]
                c += 1
            p += 1

        return c


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(5, s.removeDuplicates(array))
        self.assertEqual([0, 1, 2, 3, 4], array[:5])

        s = Solution()
        array = [0]
        self.assertEqual(1, s.removeDuplicates(array))
        self.assertEqual([0], array[:1])

        s = Solution()
        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]
        self.assertEqual(5, s.removeDuplicates(array))
        self.assertEqual([0, 1, 2, 3, 4], array[:5])

        s = Solution()
        array = [0, 1, 2, 3, 4, 4]
        self.assertEqual(5, s.removeDuplicates(array))
        self.assertEqual([0, 1, 2, 3, 4], array[:5])

        s = Solution()
        array = []
        self.assertEqual(0, s.removeDuplicates(array))
        self.assertEqual([], array[:0])


if __name__ == "__main__":
    unittest.main()
