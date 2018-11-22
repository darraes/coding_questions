from collections import deque


def count_paths(target, start, cache):
    if start == target:
        return 1

    if start in cache:
        return cache[start]

    count = 0
    if start[0] <= target[0]:
        count += count_paths(target, (start[0] + 1, start[1]), cache)
    if start[1] <= target[1]:
        count += count_paths(target, (start[0], start[1] + 1), cache)

    cache[start] = count
    return count


def find_path(target, start, off_limits, limit):
    came_from = {start : None}

    queue = deque()
    queue.append(start)
    found = False

    while len(queue) > 0:
        current = queue.popleft()

        if current == target:
            found = True
            break

        hops = []
        if current[0] < limit[0]:
            hops.append((current[0] + 1, current[1]))
        if current[1] < limit[1]:
            hops.append((current[0], current[1] + 1))

        for next_hop in hops:
            if next_hop not in came_from and next_hop not in off_limits:
                came_from[next_hop] = current
                queue.append(next_hop)
    
    if not found:
        return None

    path = deque()
    current = target
    while current:
        path.appendleft(current)
        current = came_from[current]
    return path


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        self.assertEqual(35, count_paths((3, 4), (0, 0), {}))


    def test_2(self):
        print(find_path((3, 4), (0, 0), [(0, 1), (2, 1)], (5, 5)))


if __name__ == '__main__':
    unittest.main()