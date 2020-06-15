from collections import deque


def find_order(words):
    in_degree, graph = {}, {}

    for word in words:
        for char in word:
            if char not in in_degree:
                in_degree[char] = 0
                graph[char] = []

    for i in range(1, len(words)):
        for j in range(min(len(words[i - 1]), len(words[i]))):
            if words[i - 1][j] != words[i][j]:
                in_degree[words[i][j]] += 1
                graph[words[i - 1][j]].append(words[i][j])
                break

    queue = deque([k for k, v in in_degree.items() if v == 0])

    result = []
    while queue:
        u = queue.popleft()
        result.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return "".join(result)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
