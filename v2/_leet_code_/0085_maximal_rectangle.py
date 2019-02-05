class Solution:
    def maximalRectangle(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = 1 if matrix[i][j] == "1" else 0

        max_rect = 0
        for i in range(len(matrix)):
            if i > 0:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 1:
                        matrix[i][j] += matrix[i - 1][j]

            max_rect = max(max_rect, self.largest_rect_histogram(matrix[i]))
        return max_rect

    def largest_rect_histogram(self, heights):
        def restricted_largest(heights, i, j):
            if i > j:
                return 0
            if i == j:
                return heights[i]

            cur_min = cur_min_idx = -1
            for idx in range(i, j + 1):
                if cur_min == -1 or heights[idx] < cur_min:
                    cur_min = heights[idx]
                    cur_min_idx = idx

            return max(
                cur_min * (j - i + 1),
                restricted_largest(heights, i, cur_min_idx - 1),
                restricted_largest(heights, cur_min_idx + 1, j),
            )

        return restricted_largest(heights, 0, len(heights) - 1)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            6,
            s.maximalRectangle(
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
