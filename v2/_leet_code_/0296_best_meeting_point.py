class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        people_x = []
        people_y = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    people_x.append(i)
                    people_y.append(j)

        people_x.sort()
        people_y.sort()

        best_point = (people_x[len(people_x) // 2], people_y[len(people_y) // 2])

        distance = 0
        for x in people_x:
            distance += abs(best_point[0] - x)
        for y in people_y:
            distance += abs(best_point[1] - y)

        return distance


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        self.assertEqual(6, s.minTotalDistance(grid))


if __name__ == "__main__":
    unittest.main()
