class Solution:
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        while V > 0:
            V -= 1
            lower_left = K
            for i in range(K, -1, -1):
                if heights[i] > heights[lower_left]:
                    break
                if heights[i] < heights[lower_left]:
                    lower_left = i

            if lower_left != K:
                heights[lower_left] += 1
                continue

            lower_right = K
            for i in range(K, len(heights)):
                if heights[i] > heights[lower_right]:
                    break
                if heights[i] < heights[lower_right]:
                    lower_right = i

            heights[lower_right] += 1
        return heights


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [4, 4, 4, 4, 3, 3, 3, 3, 3, 4, 3, 2, 1],
            s.pourWater([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1], 10, 2),
        )

        self.assertEqual(
            [2, 2, 2, 3, 2, 2, 2], s.pourWater(heights=[2, 1, 1, 2, 1, 2, 2], V=4, K=3)
        )


if __name__ == "__main__":
    unittest.main()
