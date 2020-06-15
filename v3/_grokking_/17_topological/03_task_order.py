from collections import deque


def find_order(tasks, prerequisites):
    task_order = []

    in_degree, graph = {}, {}
    for n in range(tasks):
        in_degree[n] = 0
        graph[n] = []

    for u, v in prerequisites:
        in_degree[v] += 1
        graph[u].append(v)

    queue = deque([k for k, v in in_degree.items() if v == 0])
    while queue:
        u = queue.popleft()
        task_order.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return task_order


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print(
        "Is scheduling possible: "
        + str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))
    )


main()
