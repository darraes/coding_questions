from collections import deque


class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        painted = {}
        for n in range(len(graph)):
            if n not in painted:
                # Beginning of a transversal. We can paint it any way
                painted[n] = 0
                queue = deque([n])
                while len(queue) > 0:
                    vertex = queue.popleft()

                    for neighbor in graph[vertex]:
                        if neighbor in painted and painted[vertex] == painted[neighbor]:
                            return False
                        elif neighbor not in painted:
                            # Since there are only 2 colors, we must alternate
                            painted[neighbor] = 0 if painted[vertex] else 1
                            queue.append(neighbor)

        return True


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertFalse(
            s.isBipartite(
                [
                    [],
                    [2, 4, 6],
                    [1, 4, 8, 9],
                    [7, 8],
                    [1, 2, 8, 9],
                    [6, 9],
                    [1, 5, 7, 8, 9],
                    [3, 6, 9],
                    [2, 3, 4, 6, 9],
                    [2, 4, 5, 6, 7, 8],
                ]
            )
        )
        self.assertTrue(s.isBipartite([[1], [0, 3], [3], [1, 2]]))
        self.assertTrue(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
        self.assertFalse(s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))


if __name__ == "__main__":
    unittest.main()
