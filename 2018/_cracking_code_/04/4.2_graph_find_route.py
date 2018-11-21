from collections import deque

class Node:
  def __init__(self, name, edges):
    self.name = name
    self.edges = edges


class Graph:
  def __init__(self, nodes):
    self.nodes = nodes


  def has_route(self, start, end):
    visited = set()

    path = deque()
    path.append(self.nodes[start])

    while len(path) > 0:
      cur_node = path.popleft()
      if cur_node.name == end:
        return True

      visited.add(cur_node.name)

      for neighbor in cur_node.edges:
        if neighbor not in visited:
          path.append(self.nodes[neighbor])

    return False



###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        nodes = {
           "a": Node("a", ["b", "c"]),
           "b": Node("b", ["d"]),
           "c": Node("c", ["e", "f"]),
           "d": Node("d", []),
           "e": Node("e", ["g"]),
           "f": Node("f", []),
           "g": Node("g", []),
           "s": Node("s", ["z"]),
           "z": Node("z", []),
        }
        g = Graph(nodes)
        self.assertTrue(g.has_route("a", "g"))
        self.assertFalse(g.has_route("b", "g"))
        self.assertFalse(g.has_route("a", "z"))


if __name__ == '__main__':
    unittest.main()