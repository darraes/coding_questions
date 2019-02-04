# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def cloneGraph(self, node):
        def clone(node, cloned):
            if not node:
                return None

            if node in cloned:
                return cloned[node]

            cloned_node = UndirectedGraphNode(node.label)
            cloned[node] = cloned_node
            for n in node.neighbors:
                cloned_node.neighbors.append(clone(n, cloned))

            return cloned_node

        return clone(node, {})


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        registry = {}

        registry["a"] = UndirectedGraphNode("a")
        registry["b"] = UndirectedGraphNode("b")
        registry["c"] = UndirectedGraphNode("c")
        registry["d"] = UndirectedGraphNode("d")

        registry["a"].neighbors.append(registry["b"])
        registry["a"].neighbors.append(registry["c"])
        registry["b"].neighbors.append(registry["d"])
        registry["d"].neighbors.append(registry["c"])

        s.cloneGraph(registry["a"])


if __name__ == "__main__":
    unittest.main(exit=False)
