def topological_sort(vertices, edges):
    sortedOrder = []

    in_degree, graph = {}, {}
    for n in range(vertices):
        in_degree[n] = 0
        graph[n] = []

    for u, v in edges:
        in_degree[v] += 1
        graph[u].append(v)

    while in_degree:
        ready = {k: v for k, v in in_degree.items() if v == 0}

        if len(ready) == 0:
            raise "cycle"

        for k, _ in ready.items():
            del in_degree[k]
            sortedOrder.append(k)

            for v in graph[k]:
                in_degree[v] -= 1

    return sortedOrder


def main():
    print(
        "Topological sort: "
        + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
    )
    print(
        "Topological sort: "
        + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
    )
    print(
        "Topological sort: "
        + str(
            topological_sort(
                7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]
            )
        )
    )


main()
