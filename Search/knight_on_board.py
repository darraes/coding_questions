# Question http://www.careercup.com/question?id=5683798268182528

from collections import deque


def in_bounds(x, y, xb, yb):
    return x <= xb and y <= yb


def movements(x, y, mov):
    return [(x - 1, y - 2, mov), 
            (x + 1, y - 2, mov), 
            (x - 2, y - 1, mov), 
            (x + 2, y - 1, mov), 
            (x - 2, y + 1, mov), 
            (x + 2, y + 1, mov), 
            (x - 1, y + 2, mov), 
            (x + 1, y + 2, mov)]

def filter (list, xbounds, ybounds):
    return [i for i in list if (i[0] <= xbounds and i[1] <= ybounds and i[0] >= 0 and i[1] >= 0)]


def shorter_path(x, y, xtarget, ytarget, xbounds, ybounds):
    visited = dict()
    queue = deque()
    queue.append((x, y, 0))

    while (len(queue) > 0):
        current = queue.popleft()

        if (current[0] == xtarget and current[1] == ytarget): return current[2] 
        
        visited[(current[0], current[1])] = True

        movs = movements(current[0], current[1], current[2] + 1)
        movs = filter(movs, xbounds, ybounds)
        movs = [i for i in movs if not visited.has_key((i[0], i[1]))]

        queue.extend(movs)

    return -1

#Entry
print shorter_path(0, 0, 6, 6, 8, 8)