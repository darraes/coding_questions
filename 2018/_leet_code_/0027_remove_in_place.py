class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        c = 0
        p = len(nums) - 1
        while c <= p:
            if nums[c] != val:
                c += 1
                continue

            tmp = nums[c]
            nums[c] = nums[p]
            nums[p] = tmp
            p -= 1

        return p + 1


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(7, s.removeElement(array, 1))
        self.assertEqual([0, 0, 4, 3, 3, 2, 2, 1, 1, 1], array)

        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(8, s.removeElement(array, 0))
        self.assertEqual([4, 3, 1, 1, 1, 2, 2, 3, 0, 0], array)

        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.assertEqual(9, s.removeElement(array, 4))
        self.assertEqual([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], array)

        array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3]
        self.assertEqual(7, s.removeElement(array, 3))
        self.assertEqual([0, 0, 1, 1, 1, 2, 2, 3, 3, 3], array)

        array = [2]
        self.assertEqual(1, s.removeElement(array, 3))
        self.assertEqual([2], array)

        array = [2]
        self.assertEqual(0, s.removeElement(array, 2))
        self.assertEqual([2], array)


if __name__ == "__main__":
    unittest.main()
