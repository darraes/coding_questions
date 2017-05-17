from collections import deque

class PriorityQueue(object):
    def __init__(self, comparator):
        self._heap = [0]
        self._elements_count = 0
        self.compare = comparator

    
    """Checks if the heap is empty"""
    def is_empty(self):
        return self._elements_count == 0

    def __len__(self):
        return self._elements_count


    """Bubbles up a misplaced element at the end of the heap
       This function makes sure that the last element gets to its right 
       position
    """
    def _heapfy(self):
        target_i = self._elements_count

        while target_i / 2 > 0:
            parent_i = target_i / 2
            if self.compare(self._heap[parent_i], self._heap[target_i]): break

            target = self._heap[target_i]
            self._heap[target_i] = self._heap[parent_i]
            self._heap[parent_i] = target

            target_i = parent_i


    """Inserts an element to the heap"""
    def insert(self, element):
        self._heap.append(element)
        self._elements_count += 1
        self._heapfy()


    """Pops an element from the heap"""
    def pop(self):
        if self._elements_count == 0: raise ValueError("Empty Heap")

        result = self._heap[1]
        self._heap[1] = self._heap[self._elements_count]
        self._elements_count -= 1
        del self._heap[-1]

        self._adjust_priority(1)
        return result


    """Sends a misplaced element on the very first position of the heap to its right position
       so that the heap ordering property is not afected
    """
    def _adjust_priority(self, index):
        if index >= self._elements_count: return;

        while 2 * index <= self._elements_count:
            priority_child = self._max_pri_index(2 * index, 2 * index + 1)

            if not self.compare(self._heap[index], self._heap[priority_child]):
                tmp = self._heap[priority_child]
                self._heap[priority_child] = self._heap[index]
                self._heap[index] = tmp
                
            index = priority_child       


    """Finds the index that contains the element with highest priority"""
    def _max_pri_index(self, left, right):
        if right > self._elements_count or \
            self.compare(self._heap[left], self._heap[right]):
            return left
        else:
            return right

""" End PriorityQueue """


####### BOMB PROBLEM 
#http://www.careercup.com/question?id=5681111363485696

def compare_cost(left, right):
    if left[0] < right[0]: return True
    elif left[0] == right[0] and left[1] > right[1]: return True
    return False

def in_scope(matrix, position):
    return position[0] < 4 and position[1] < 4 and position[0] >= 0 and position[1] >= 0

def has_bomb(matrix, position):
    if position == (2, 3) or position == (3, 2): return True
    return False

def print_path(came_from, goal):
    path = deque()
    while came_from.has_key(goal):
        path.append(goal)
        goal = came_from[goal]

    while len(path) > 0:
        print path.popleft()

def solve(matrix, goal, bombs):
    queue = PriorityQueue(lambda p, c: p[1][0] < c[1][0] if p[1][0] != c[1][0] else p[1][1] >= c[1][1])

    came_from = dict()
    cost_so_far = dict()
    cost_so_far[(0, 0)] = (0, bombs)
    queue.insert(((0, 0), (0, bombs)))

    while len(queue) > 0:
        current = queue.pop()

        if current[0] == goal:
            print_path(came_from, goal)
            return current[1]

        move_right = (current[0][0], current[0][1] + 1)
        move_left = (current[0][0], current[0][1] - 1)
        move_down = (current[0][0] + 1, current[0][1])
        move_up = (current[0][0] - 1, current[0][1])
        moves = [move_right, move_left, move_down, move_up]

        neighbors = []
        for move in moves:
            if in_scope(matrix, move):
                if has_bomb(matrix, move) and current[1][1] > 0:
                    neighbors.append((move, (current[1][0] + 1, current[1][1] - 1)))
                else:
                    neighbors.append((move, (current[1][0] + 1, current[1][1])))

        for neighbor in neighbors:
            if not cost_so_far.has_key(neighbor[0]) or compare_cost(neighbor[1], cost_so_far[neighbor[0]]):
                cost_so_far[neighbor[0]] = (neighbor[1][0], neighbor[1][1])
                came_from[neighbor[0]] = current[0]
                queue.insert(neighbor)
            
    return (-1, -1)

print solve([], (3, 3), 2)

