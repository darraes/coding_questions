def print_lines(matrix):
    for line in matrix:
        print(line)


from collections import deque


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    count += 1
                    self.flood_fill(grid, x, y)
        return count

    def flood_fill(self, grid, x, y):
        queue = deque([(x, y)])
        visited = set((x, y))

        while len(queue) > 0:
            c_x, c_y = queue.popleft()
            grid[c_x][c_y] = "2"

            for (n_x, n_y) in [
                (c_x + 1, c_y),
                (c_x, c_y + 1),
                (c_x - 1, c_y),
                (c_x, c_y - 1),
            ]:
                if (
                    self.in_bounds(grid, n_x, n_y)
                    and grid[n_x][n_y] == "1"
                    and (n_x, n_y) not in visited
                ):
                    visited.add((n_x, n_y))
                    queue.append((n_x, n_y))

    def in_bounds(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[x])


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        full_map = [
            ["0", "0", "0", "0", "0", "0", "1", "1", "0"],
            ["0", "0", "0", "0", "0", "0", "1", "1", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "1", "0", "0", "0", "0"],
            ["0", "1", "0", "1", "1", "1", "0", "0", "0"],
            ["0", "1", "0", "0", "0", "1", "0", "0", "0"],
            ["0", "1", "0", "0", "0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ]
        self.assertEqual(3, s.numIslands(full_map))

        full_map = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.assertEqual(3, s.numIslands(full_map))

        full_map = [
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "0",
                "1",
                "1",
            ],
            [
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
            ],
            [
                "1",
                "0",
                "1",
                "1",
                "1",
                "0",
                "0",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "0",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
            ],
            [
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "0",
                "1",
                "1",
                "1",
                "1",
                "0",
                "0",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
            [
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
                "1",
            ],
        ]
        self.assertEqual(1, s.numIslands(full_map))


if __name__ == "__main__":
    unittest.main()
