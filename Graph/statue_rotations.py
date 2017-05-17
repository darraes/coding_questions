# http://www.careercup.com/question?id=5380513791475712

#N = 0, E = 1, S = 2, W = 3

from collections import deque

def move(statues, positions):
    for p in positions:
        statues[p] = (statues[p] + 1) % 4
    return statues

def stringfy(statues):
    s = ""
    for i in statues:
        s += "{}".format(i)
    return s

def is_solved(statues):
    for i in range(1, len(statues)):
        if statues[i - 1] != statues[i]: return False

    return True

def code(txtStatues):
    statues = []
    for p in txtStatues:
        if p == 'N': statues.append(0)
        elif p == 'E': statues.append(1)
        elif p == 'S': statues.append(2)
        else: statues.append(3)
    return statues

def shortest_path(txtStatues, moves):
    #TODO validations
    statues = code(txtStatues)
    visited = set()
    queue = deque()
    queue.append((0, statues))

    while len(queue) > 0:
        node = queue.popleft();
        key = stringfy(node[1])

        if key not in visited:
            visited.add(key)
            if is_solved(node[1]): return node[0]
            else:
                for m in moves:
                   next = move([s for s in node[1]], m)
                   keyNext = stringfy(next)
                   if keyNext not in visited:
                       queue.append((node[0] + 1, next))
    return -1

#
print shortest_path("NNSEWSWN", [[0, 1],
                                 [0, 1, 2],
                                 [1, 4, 5, 6],
                                 [2, 5],
                                 [3, 5],
                                 [3, 7],
                                 [5, 7],
                                 [6, 7]])
