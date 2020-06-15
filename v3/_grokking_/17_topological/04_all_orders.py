from collections import deque


def print_orders(tasks, prerequisites):
    in_degree, graph = tasks * [0], {}

    for i in range(tasks):
        graph[i] = []

    for u, v in prerequisites:
        in_degree[v] += 1
        graph[u].append(v)

    ready = [k for k, v in enumerate(in_degree) if v == 0]

    def dfs(result, ready):
        nonlocal tasks, in_degree, graph

        if len(result) == tasks:
            print(result)

        for i in range(len(ready)):
            u = ready[i]
            next_ready = ready[:i] + ready[i + 1 :]

            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    next_ready.append(v)

            dfs(result + [u], next_ready)

            for v in graph[u]:
                in_degree[v] += 1

    dfs([], ready)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()