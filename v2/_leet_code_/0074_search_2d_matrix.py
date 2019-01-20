from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        heads = [matrix[i][0] for i in range(len(matrix)) if len(matrix[i]) > 0]
        idx = bisect_left(heads, target)

        if not heads or idx < 0:
            return False
        if idx < len(matrix) and matrix[idx][0] == target:
            return True
        if idx == 0:
            return False

        idx -= 1
        jdx = bisect_left(matrix[idx], target)
        return jdx < len(matrix[idx]) and matrix[idx][jdx] == target


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        self.assertTrue(s.searchMatrix(matrix, 1))
        self.assertTrue(s.searchMatrix(matrix, 3))
        self.assertTrue(s.searchMatrix(matrix, 5))
        self.assertTrue(s.searchMatrix(matrix, 7))
        self.assertTrue(s.searchMatrix(matrix, 10))
        self.assertTrue(s.searchMatrix(matrix, 11))
        self.assertTrue(s.searchMatrix(matrix, 16))
        self.assertTrue(s.searchMatrix(matrix, 20))
        self.assertTrue(s.searchMatrix(matrix, 23))
        self.assertTrue(s.searchMatrix(matrix, 30))
        self.assertTrue(s.searchMatrix(matrix, 34))
        self.assertTrue(s.searchMatrix(matrix, 50))

        self.assertFalse(s.searchMatrix(matrix, 0))
        self.assertFalse(s.searchMatrix(matrix, 4))
        self.assertFalse(s.searchMatrix(matrix, 9))
        self.assertFalse(s.searchMatrix(matrix, 12))
        self.assertFalse(s.searchMatrix(matrix, 21))
        self.assertFalse(s.searchMatrix(matrix, 35))
        self.assertFalse(s.searchMatrix(matrix, 51))

        matrix = [[]]
        self.assertFalse(s.searchMatrix(matrix, 1))


if __name__ == "__main__":
    unittest.main()
