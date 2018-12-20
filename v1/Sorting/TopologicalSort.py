# http://www.careercup.com/question?id=5717669093310464

from collections import deque

class Graph(object):
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2

    def __init__(self, vertices):
        self._vertices = vertices
        self._dependants = [None]*vertices
        self._depends_on = [None]*vertices 
    
    def add_edge(self, v_origim, v_dest):
        """Adds an edge from one vertice to another"""

        if self._dependants[v_origim] is None:
            self._dependants[v_origim] = []
        self._dependants[v_origim].append(v_dest)

        if self._depends_on[v_dest] is None:
            self._depends_on[v_dest] = []
        self._depends_on[v_dest].append(v_origim)
         
    
    def topological_sort_edge(self):
        """ Other type of toposort implementation. This uses an inverted adjacent list to keep
        track of what dependencies a given node still have considering that previous node are built
        and therefore can be ignored as a dependency
        """
        projects = deque()

        #find all nodes that do not depend on any other node and clone the 
        #inverted edge adjacent list
        available = deque([n for n in range(6) if self._depends_on[n] is None])
        depends_on = self._clone_depends_on()

        while len(available) > 0:
            node = available.popleft()
            projects.append(node)

            if self._dependants[node] is not None:
                for dependant in self._dependants[node]:

                    #remove the dependency and check if the node has no dependecies and therefore
                    #can be built
                    depends_on[dependant].remove(node)
                    if depends_on[dependant] is None or len(depends_on[dependant]) == 0:
                        available.append(dependant)

        return list(projects)


    def _clone_depends_on(self):
        """ Clones the _depends_on list to avoid destructing the list when 
        topological_sort_edge gets called
        """
        result = [None]*self._vertices
        for i in range(self._vertices):
            if self._depends_on[i] is not None:
                result[i] = self._depends_on[i][:]

        return result
                
    
    def topologial_sort_stk(self):
        """Returns a topologially sorted list with the vertices of this graph"""
        path = deque()
        track = [Graph.NOT_VISITED] * self._vertices

        for i in range(self._vertices):
            if track[i] == Graph.NOT_VISITED:
                self._toposort_stk(i, path, track)

        path.reverse()
        return list(path)
    
    def _toposort_stk(self, vertice, path, track):
        """Actual recursive DFS sorting function"""
        if track[vertice] == Graph.VISITING: raise "Cycle Detected"

        track[vertice] = Graph.VISITING

        if self._dependants[vertice] is not None:
            for adj in self._dependants[vertice]:
                if track[adj] == Graph.NOT_VISITED:
                    self._toposort_stk(adj, path, track)

        track[vertice] = Graph.VISITED
        path.append(vertice)


g = Graph(6)
g.add_edge(0, 1);
g.add_edge(0, 2);
g.add_edge(0, 4);
g.add_edge(1, 3);
g.add_edge(2, 3);
g.add_edge(2, 4);
g.add_edge(3, 5);
g.add_edge(4, 5);
print g.topologial_sort_stk()
print g.topological_sort_edge()

# 0 depends on 1
g = Graph(4)
g.add_edge(1, 0);
g.add_edge(2, 1);
g.add_edge(3, 1);
g.add_edge(3, 2);
print g.topologial_sort_stk()