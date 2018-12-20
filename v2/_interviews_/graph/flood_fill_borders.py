from collections import deque


def print_lines(matrix):
    for line in matrix:
        print(line)


def in_bounds(full_map, x, y):
    return 0 <= x < len(full_map) and 0 <= y < len(full_map[x])


def flood_fill(full_map, x, y, new_color):
    color = full_map[x][y]

    to_visit = deque([(x, y)])
    visited = set()

    while len(to_visit) > 0:
        cur_x, cur_y = to_visit.popleft()
        visited.add((cur_x, cur_y))

        vh_neighbors = [
            (x, y)
            for (x, y) in [
                (cur_x + 1, cur_y),
                (cur_x, cur_y + 1),
                (cur_x - 1, cur_y),
                (cur_x, cur_y - 1),
            ]
            if in_bounds(full_map, x, y)
        ]
        d_neighbors = [
            (x, y)
            for (x, y) in [
                (cur_x - 1, cur_y - 1),
                (cur_x + 1, cur_y - 1),
                (cur_x - 1, cur_y + 1),
                (cur_x + 1, cur_y + 1),
            ]
            if in_bounds(full_map, x, y)
        ]

        for neighbor in vh_neighbors:
            if full_map[neighbor[0]][neighbor[1]] != color:
                full_map[neighbor[0]][neighbor[1]] = new_color
            elif (
                full_map[neighbor[0]][neighbor[1]] == color
                and (neighbor[0], neighbor[1]) not in visited
            ):
                to_visit.append((neighbor[0], neighbor[1]))
        for neighbor in d_neighbors:
            if (
                full_map[neighbor[0]][neighbor[1]] == color
                and (neighbor[0], neighbor[1]) not in visited
            ):
                to_visit.append((neighbor[0], neighbor[1]))


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        full_map = [
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        flood_fill(full_map, 4, 4, 5)

        solution = [
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0],
            [0, 0, 0, 5, 1, 5, 0, 0],
            [0, 1, 5, 1, 1, 1, 5, 0],
            [0, 1, 0, 5, 5, 1, 5, 0],
            [0, 1, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        print_lines(full_map)
        self.assertEqual(solution, full_map)


if __name__ == "__main__":
    unittest.main()
