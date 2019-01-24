from collections import deque

def print_lines(matrix):
    for line in matrix:
        print(line)


def in_bounds(full_map, x, y):
    return 0 <= x < len(full_map) and 0 <= y < len(full_map[x])


def flood_fill(full_map, start_x, start_y):
    if full_map[start_x][start_y] == 0:
        return

    to_visit = deque([(start_x, start_y)])
    visited = set((start_x, start_y))
    while len(to_visit) > 0:
        cur_x, cur_y = to_visit.popleft()

        full_map[cur_x][cur_y] = 2
        for neighbor in [
            (cur_x + 1, cur_y),
            (cur_x, cur_y + 1),
            (cur_x - 1, cur_y),
            (cur_x, cur_y - 1),
            (cur_x - 1, cur_y - 1),
            (cur_x + 1, cur_y - 1),
            (cur_x - 1, cur_y + 1),
            (cur_x + 1, cur_y + 1),
        ]:
            if (
                in_bounds(full_map, neighbor[0], neighbor[1])
                and full_map[neighbor[0]][neighbor[1]] == 1
                and (neighbor[0], neighbor[1]) not in visited
            ):
                visited.add((neighbor[0], neighbor[1]))
                to_visit.append(neighbor)

def count_islands(full_map):
    islands = 0
    for x in range(len(full_map)):
        for y in range(len(full_map[x])):
            if full_map[x][y] == 1:
                islands += 1
                flood_fill(full_map, x, y)
    return islands


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
        self.assertEqual(3, count_islands(full_map))
        print_lines(full_map)


if __name__ == "__main__":
    unittest.main()
