class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        s2 = set(nums2)

        return [e for e in s1 if e in s2]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual([2], s.intersection([1, 2, 2, 1], [2, 2]))
        self.assertEqual([3], s.intersection([1, 2, 3], [3]))
        self.assertEqual([3], s.intersection([3], [1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
