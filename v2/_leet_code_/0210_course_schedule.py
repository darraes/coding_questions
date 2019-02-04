from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for pre_r in prerequisites:
            after, before = pre_r[0], pre_r[1]
            graph[after].append(before)

        res = []
        visited = set()
        visiting = set()

        def dfs(n):
            nonlocal graph, res, visited, visiting
            if n in visiting:
                raise "Cycle"

            visiting.add(n)

            for dependance in graph[n]:
                if dependance not in visited:
                    dfs(dependance)
            res.append(n)

            visited.add(n)
            visiting.remove(n)

        try:
            for n in range(numCourses):
                if n not in visited:
                    dfs(n)
        except:
            return []

        return res


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([], s.findOrder(2, [[1, 0], [0, 1]]))
        self.assertEqual([0, 1], s.findOrder(2, [[1, 0]]))
        self.assertEqual([0, 1, 2, 3], s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
        self.assertEqual([2, 1, 0], s.findOrder(3, [[0, 1], [0, 2], [1, 2]]))
        self.assertEqual([1, 0, 2], s.findOrder(3, [[0, 1]]))
        self.assertEqual([1, 0, 2], s.findOrder(3, [[0, 1], [2, 1]]))

        # self.assertEqual(True, s.findOrder2(3, [[0, 1], [0, 2], [1, 2]]))
        # self.assertEqual(False, s.findOrder2(2, [[1, 0], [0, 1]]))
        # self.assertEqual(True, s.findOrder2(2, [[1, 0]]))
        # self.assertEqual(False, s.findOrder2(3, [[0, 1], [1, 2], [2, 0]]))
        # self.assertEqual(True, s.findOrder2(3, [[0, 1]]))
        # self.assertEqual(True, s.findOrder2(3, [[0, 1], [2, 1]]))


if __name__ == "__main__":
    unittest.main(exit=False)
