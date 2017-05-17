class PriorityQueue(object):
    def __init__(self, comparator):
        self._heap = [0]
        self._elements_count = 0
        self.compare = comparator

    
    """Checks if the heap is empty"""
    def is_empty(self):
        return self._elements_count == 0


    """Gets the length of the queue as of now"""
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


pq = PriorityQueue(lambda p, c: p < c)

pq.insert(34)
pq.insert(10)
pq.insert(21)
pq.insert(25)
pq.insert(12)
pq.insert(6)
pq.insert(9)

while not pq.is_empty():
    print pq.pop()