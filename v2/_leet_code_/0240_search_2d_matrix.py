class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        row = 0
        col = len(matrix[row]) - 1

        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        s = Solution()
        self.assertTrue(s.searchMatrix(matrix, 5))
        self.assertTrue(s.searchMatrix(matrix, 15))
        self.assertTrue(s.searchMatrix(matrix, 18))
        self.assertTrue(s.searchMatrix(matrix, 1))
        self.assertTrue(s.searchMatrix(matrix, 30))

        self.assertFalse(s.searchMatrix(matrix, 31))
        self.assertFalse(s.searchMatrix(matrix, 40))
        self.assertFalse(s.searchMatrix(matrix, -1))
        self.assertFalse(s.searchMatrix(matrix, 0))
        self.assertFalse(s.searchMatrix([], 0))



if __name__ == "__main__":
    unittest.main()
