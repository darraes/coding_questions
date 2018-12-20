from queue import PriorityQueue
from collections import deque


def cost(graph, v_from, v_to):
    if v_from in graph:
        if v_to in graph[v_from]:
            return graph[v_from][v_to]
    return None


def heuristic(graph, v_from, v_to):
    return 0


def best_path(v_from, v_to, graph):
    came_from = {v_from: None}
    cost_so_far = {v_from: 0}
    frontier = PriorityQueue()

    frontier.put((cost_so_far[v_from], v_from))

    while not frontier.empty():
        _, v_current = frontier.get()

        if v_current == v_to:
            break

        for v_next, edge_cost in graph[v_current].items():
            cost_to_next = edge_cost + cost_so_far[v_current]
            if v_next not in cost_so_far or cost_to_next < cost_so_far[v_next]:
                cost_so_far[v_next] = cost_to_next
                came_from[v_next] = v_current
                priority = cost_to_next + heuristic(graph, v_next, v_to)
                frontier.put((priority, v_next))

    path = deque()
    hop_back = v_to
    while hop_back:
        path.appendleft(hop_back)
        hop_back = came_from[hop_back]

    for hop in path:
        print(hop)



###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("===================")
        graph = {"A": {"B": 3, "D": 1, "E": 3},
                 "B": {"F": 5, "D": 7, "E": 2},
                 "D": {"E": 1, "F": 4, "B": 1},
                 "E": {"F": 1},
                 "F": {}}
        best_path("A", "B", graph)

if __name__ == '__main__':
    unittest.main()