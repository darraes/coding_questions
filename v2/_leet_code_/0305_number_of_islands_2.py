class DisjointSets:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        self.count = 0

    def add_set(self, r, c):
        self.parents[(r, c)] = (r, c)
        self.rank[(r, c)] = 1
        self.count += 1

    def parent(self, r, c):
        if self.parents[(r, c)] == (r, c):
            return (r, c)

        self.parents[(r, c)] = self.parent(*self.parents[self.parents[(r, c)]])
        return self.parents[(r, c)]

    def union(self, r1, c1, r2, c2):
        p1 = self.parent(r1, c1)
        p2 = self.parent(r2, c2)

        if p1 == p2:
            return

        self.count -= 1

        r1 = self.rank[(r1, c1)]
        r2 = self.rank[(r2, c2)]

        if r1 > r2:
            self.parents[p2] = p1
        elif r2 > r1:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.rank[p1] += 1


class Solution:
    def neighbors(self, x, y, m, n):
        res = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        return [(x, y) for (x, y) in res if 0 <= x < m and 0 <= y < n]

    def numIslands2(self, m, n, positions):
        res = []
        grid = [[0 for _ in range(n)] for _ in range(m)]
        dsu = DisjointSets()
        for position in positions:
            grid[position[0]][position[1]] = 1
            dsu.add_set(position[0], position[1])

            for n_x, n_y in self.neighbors(position[0], position[1], m, n):
                if grid[n_x][n_y]:
                    dsu.union(position[0], position[1], n_x, n_y)

            res.append(dsu.count)

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
