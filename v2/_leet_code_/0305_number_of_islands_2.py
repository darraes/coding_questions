from collections import deque


class Solution:
    def print_grid(self, grid):
        for l in grid:
            print(l)
        print()

    def neighbors(self, x, y, m, n):
        res = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        return [(x, y) for (x, y) in res if 0 <= x < m and 0 <= y < n]

    def flood_fill(self, color, x, y, m, n, grid):
        queue = deque([(x, y)])
        visited = set([(x, y)])

        while len(queue) > 0:
            cur_x, cur_y = queue.popleft()
            grid[cur_x][cur_y] = color

            for (nx, ny) in [
                (nx, ny)
                for (nx, ny) in self.neighbors(cur_x, cur_y, m, n)
                if grid[nx][ny] != 0
                and grid[nx][ny] != color
                and (nx, ny) not in visited
            ]:
                queue.append((nx, ny))
                visited.add((nx, ny))

        return

    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        grid = [[0 for _ in range(n)] for _ in range(m)]
        color = 1
        islands = 0

        for position in positions:
            lands = [
                (nx, ny)
                for (nx, ny) in self.neighbors(position[0], position[1], m, n)
                if grid[nx][ny] != 0
            ]

            if len(lands) == 0:
                grid[position[0]][position[1]] = color
                color += 1
                islands += 1
            else:
                grid[position[0]][position[1]] = grid[lands[0][0]][lands[0][1]]
                for edge_x, edge_y in lands[1:]:
                    if grid[position[0]][position[1]] != grid[edge_x][edge_y]:
                        islands -= 1
                        self.flood_fill(
                            grid[position[0]][position[1]], edge_x, edge_y, m, n, grid
                        )
            res.append(islands)

        return res


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(
            [1, 1, 2, 3],
            s.numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]]),
        )

        self.assertEqual(
            [1, 1, 2, 2],
            s.numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 2]]),
        )

        self.assertEqual(
            [1, 1, 2, 2, 1],
            s.numIslands2(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 2], [0, 2]]),
        )

        self.assertEqual(
            [1, 1, 2, 3, 2, 1, 1],
            s.numIslands2(
                m=3,
                n=3,
                positions=[[0, 0], [0, 1], [1, 2], [2, 1], [2, 2], [0, 2], [1, 1]],
            ),
        )


if __name__ == "__main__":
    unittest.main()
