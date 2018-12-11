class Solution:
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights or len(heights) == 0:
            return 0

        max_left = [0] * len(heights)
        max_right = [0] * len(heights)

        max_left[0] = heights[0]
        for i in range(1, len(heights)):
            max_left[i] = max(max_left[i - 1], heights[i])

        i = len(heights) - 1
        max_right[i] = heights[i]
        i -= 1
        while i >= 0:
            max_right[i] = max(max_right[i + 1], heights[i])
            i -= 1

        res = 0
        for i in range(len(heights)):
            res += min(max_left[i], max_right[i]) - heights[i]

        return res


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(6, s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        self.assertEqual(2, s.trap([0, 1, 0, 2, 1, 0, 1, 1, 1, 1, 1, 1]))
        self.assertEqual(1, s.trap([2, 0, 1]))
        self.assertEqual(0, s.trap([5, 4, 3, 2, 1, 0]))
        self.assertEqual(0, s.trap([1]))
        self.assertEqual(0, s.trap([0]))
        self.assertEqual(0, s.trap([0, 1]))
        self.assertEqual(0, s.trap([1, 2]))
        self.assertEqual(0, s.trap([]))


if __name__ == "__main__":
    unittest.main()
