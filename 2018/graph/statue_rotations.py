# https://www.careercup.com/question?id=5380513791475712
from collections import deque
from copy import copy

def next_rotation(code):
    if code == "N":
        return "E"
    if code == "E":
        return "S"
    if code == "S":
        return "W"
    else:
        return "N"


def move(statues, targets):
    result = copy(statues)
    for target in targets:
        result = result[0:target] \
                 + next_rotation(statues[target]) \
                 + result[target + 1:]
    return result


def same_direction(statues):
    first_direction = statues[0]
    for direction in statues:
        if direction != first_direction:
            return False
    return True


def shortest_path(statues, moves):
    step_queue = deque()
    cache = set()

    step_queue.append((statues, 0, [statues], []))

    while len(step_queue) > 0:
        step, distance, path, past_moves = step_queue.popleft()

        if same_direction(step):
            return (distance, path, past_moves)

        if distance > 50:
            return (-1, None, None)

        for m in moves:
            next_step = move(step, m)
            if next_step not in cache:
                step_queue.append(
                    (next_step, 
                     distance + 1,
                     copy(path) + [next_step],
                     copy(past_moves) + [m]))
                cache.add(next_step)

    return (-1, None, None)



###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        distance, path, exe_moves = shortest_path("NNSEWSWN", 
                                                  [[0, 1],
                                                   [0, 1, 2],
                                                   [1, 4, 5, 6],
                                                   [2, 5],
                                                   [3, 5],
                                                   [3, 7],
                                                   [5, 7],
                                                   [6, 7]])
        print distance, path, exe_moves
        self.assertEqual(6, distance)

    def test_2(self):
        distance, path, exe_moves = shortest_path("SSSSSSSS", 
                                                  [[0, 1],
                                                   [0, 1, 2],
                                                   [1, 4, 5, 6],
                                                   [2, 5],
                                                   [3, 5],
                                                   [3, 7],
                                                   [5, 7],
                                                   [6, 7]])
        print distance, path, exe_moves
        self.assertEqual(0, distance)

    def test_3(self):
        distance, path, exe_moves = shortest_path("WWNNNNNN", 
                                                  [[0, 1],
                                                   [0, 1, 2],
                                                   [1, 4, 5, 6],
                                                   [2, 5],
                                                   [3, 5],
                                                   [3, 7],
                                                   [5, 7],
                                                   [6, 7]])
        print distance, path, exe_moves
        self.assertEqual(1, distance)


if __name__ == '__main__':
    unittest.main()