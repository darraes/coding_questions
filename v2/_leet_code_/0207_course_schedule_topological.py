from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for pre_req in prerequisites:
            graph[pre_req[0]].append(pre_req[1])

        transversed = set()
        for start in [k for k, v in graph.items()]:
            if start not in transversed:
                if not self.dfs(graph, start, set(), transversed):
                    return False

        return True

    def dfs(self, graph, current, visiting, transversed):
        if current in visiting:
            return False

        visiting.add(current)
        transversed.add(current)

        for req in graph[current]:
            if not self.dfs(graph, req, visiting, transversed):
                return False

        visiting.remove(current)
        return True

    def canFinish2(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = dict([(n, 0) for n in range(numCourses)])

        for pre_req in prerequisites:
            graph[pre_req[1]].append(pre_req[0])
            indegree[pre_req[0]] += 1

        queue = deque([k for (k, n) in indegree.items() if n == 0])
        free = len(queue)

        while len(queue) > 0:
            current = queue.popleft()
            for r in graph[current]:
                indegree[r] -= 1
                if indegree[r] == 0:
                    queue.append(r)
                    free += 1

        return free == numCourses


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(False, s.canFinish(2, [[1, 0], [0, 1]]))
        self.assertEqual(True, s.canFinish(3, [[0, 1], [0, 2], [1, 2]]))
        self.assertEqual(True, s.canFinish(2, [[1, 0]]))
        self.assertEqual(False, s.canFinish(3, [[0, 1], [1, 2], [2, 0]]))
        self.assertEqual(True, s.canFinish(3, [[0, 1]]))
        self.assertEqual(True, s.canFinish(3, [[0, 1], [2, 1]]))

        self.assertEqual(True, s.canFinish2(3, [[0, 1], [0, 2], [1, 2]]))
        self.assertEqual(False, s.canFinish2(2, [[1, 0], [0, 1]]))
        self.assertEqual(True, s.canFinish2(2, [[1, 0]]))
        self.assertEqual(False, s.canFinish2(3, [[0, 1], [1, 2], [2, 0]]))
        self.assertEqual(True, s.canFinish2(3, [[0, 1]]))
        self.assertEqual(True, s.canFinish2(3, [[0, 1], [2, 1]]))


if __name__ == "__main__":
    unittest.main(exit=False)
