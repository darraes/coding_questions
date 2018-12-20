class Node(object):
    def __init__(self, key, value):
        self.next = None
        self.previous = None
        self.key = key
        self.value = value
        
    def __str__(self):
        return '{}'.format(self.value)


class LRUCache(object):
    def __init__(self, size):
        self._size = size
        self._head = None
        self._tail = None
        self._elements = dict()
        
        
    def put(self, key, value):
        if key in self._elements:
            self._elements[key].value = value
            self._move_to_front(key)
        else:
            if len(self._elements) == self._size:
                self._remove_tail()
                
            node = Node(key, value)
            if len(self._elements) > 0:
                self._add_to_front(node)
            else:
                self._head = node
                self._tail = node
            self._elements[key] = node    
        return self
        
        
    def get(self, key):
        if key in self._elements:
            self._move_to_front(key)
            return self._elements[key].value
        else:
            return None
            
            
    def _move_to_front(self, key):
        if key not in self._elements:
            raise
            
        node = self._elements[key]
        if node == self._head:                 
            return
            
        n_next = node.next
        n_prev = node.previous
        n_prev.next = n_next
        if n_next:
            n_next.previous = n_prev
        else:
            self._tail = n_prev
            
        self._add_to_front(node)
        return self
            
            
    def _add_to_front(self, node):
        if node == self._head:
            raise
            
        node.next = self._head
        node.previous = None
        if self._head:
            self._head.previous = node
        self._head = node
        return self
        
        
    def _remove_tail(self):
        old_tail = self._tail
        self._tail = old_tail.previous
        self._tail.next = None
        del self._elements[old_tail.key]
        return self
        
        
    def print_cache(self):
        str = ""
        node = self._head
        while node is not None:
            str += "({}, {}, {}) -> ".format(node.previous, node, node.next)
            node = node.next
        print str
        print "({}, {}, {}) -> ".format(self._tail.previous
                                        , self._tail, self._tail.next)
        return self
            
            
            
cache = LRUCache(3)
cache.put("a", 1)
cache.print_cache()
cache.put("b", 2)
cache.print_cache()
cache.put("c", 3)
cache.print_cache()
cache.get("a")
cache.print_cache()
cache.get("c")
cache.print_cache()
cache.get("c")
cache.print_cache()
cache.put("d", 4)
cache.print_cache()



















  
        