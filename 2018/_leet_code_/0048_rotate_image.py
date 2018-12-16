class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        layer = 0
        while layer < len(matrix) // 2:
            last = len(matrix) - layer - 1

            for i in range(layer, last):
                offset = i - layer
                top = matrix[layer][i]

                matrix[layer][i] = matrix[last - offset][layer]
                matrix[last - offset][layer] = matrix[last][last - offset]
                matrix[last][last - offset] = matrix[i][last]
                matrix[i][last] = top

            layer += 1


###############################################################
import unittest
import sys


def print_lines(X):
    for x in X:
        print(x)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        problem = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        solution = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]

        #s.rotate(problem)
        #print_lines(problem)
        #self.assertEqual(solution, problem)

        problem = [
          [ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]
        ]
        solution = [
          [15,13, 2, 5],
          [14, 3, 4, 1],
          [12, 6, 8, 9],
          [16, 7,10,11]
        ]

        s.rotate(problem)
        print_lines(problem)
        self.assertEqual(solution, problem)


if __name__ == "__main__":
    unittest.main()
