# http://www.careercup.com/question?id=5181899328716800

from collections import deque

class Glass(object):
    def __init__(self, value, row):
        self._value = value
        self._row = row
        self._connections = []
        self._fill = 0


    @staticmethod
    def new_years_eve(bottles = 1, levels = 1, glass = 1):
        if bottles < 1 or levels < 1 or glass < 1: raise ValueError()

        full_distribution = Glass._distribute(levels, bottles, 750, 250)

        if full_distribution.has_key((levels, glass)):
            return full_distribution[(levels, glass)]._fill
        else: raise ValueError("No such Level/Glass")

        
    @staticmethod
    def _distribute(levels, bottles, bottle_size, glass_size):
        graph = Glass._build_graph(1, levels)

        ml = bottles * bottle_size
        entry_node = graph[(1,1)]
        entry_node._fill = ml
        queue = deque()
        queue.append(entry_node)

        while len(queue) > 0:
            glass = queue.popleft()
            if glass._fill > glass_size:
                to_divide = glass._fill - glass_size
                glass._fill = glass_size
                for node in glass._connections:
                    node._fill += to_divide / len(glass._connections)
                    queue.append(node)

        return graph    


    @staticmethod
    def _build_graph(current_level, max_level):
        if current_level < 1: raise ValueError()

        current_nodes = Glass._level_nodes(current_level)

        result = dict()
        if current_level < max_level:
            sub_graph = Glass._build_graph(current_level + 1, max_level)
            result = sub_graph
            for node in current_nodes:
                node._connections.append(sub_graph[(current_level + 1, node._value)])
                node._connections.append(sub_graph[(current_level + 1, node._value + node._row)])
                node._connections.append(sub_graph[(current_level + 1, node._value + node._row + 1)])
        
        for node in current_nodes:
            result[(current_level, node._value)] = node
        return result


    @staticmethod
    def _level_nodes(level):
        nodes = []
        last = 0
        row = 1
        while row <= level:
            for i in range(row):
                last += 1
                nodes.append(Glass(last, row))
            row += 1
        return nodes

    @staticmethod
    def _what_row(number):
        row = 0
        current = 1

        while number > 0:
            row += 1
            for i in range (row):
                number -= 1

        return row


print Glass.new_years_eve()
print Glass.new_years_eve(bottles = 3, levels = 4, glass = 5)
print Glass.new_years_eve(bottles = 3, levels = 3, glass = 6)
print Glass.new_years_eve(bottles = 5, levels = 4, glass = 10)
print Glass.new_years_eve(bottles = 3, levels = 4, glass = 8)

for i in range(10):
    print (i, Glass._what_row(i))

