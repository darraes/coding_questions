class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        e = len(height) - 1
        max_area = 0

        while s < e:
            max_area = max(max_area, min(height[s], height[e])*(e - s))
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return max_area

###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(49, s.maxArea([1,8,6,2,5,4,8,3,7]))
        self.assertEqual(0, s.maxArea([8]))
        self.assertEqual(2, s.maxArea([2, 8]))
        self.assertEqual(6, s.maxArea([2, 1, 1, 8]))
        self.assertEqual(16, s.maxArea([4, 1, 8, 1, 4]))


if __name__ == '__main__':
    unittest.main()