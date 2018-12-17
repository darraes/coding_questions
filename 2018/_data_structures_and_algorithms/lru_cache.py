class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        return "({},{})".format(self.key, self.val)


class SimpleLinkedList(object):
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def add_as_head(self, n):
        self.size += 1
        self._add_as_head(n)

    def evict_last_if_full(self):
        if self.size == self.capacity:
            self.size -= 1
            return self._retreat_tail()

    def move_to_head(self, n):
        if n.key == self.head.key:
            return

        my_prev = n.prev
        my_next = n.next

        if my_prev:
            my_prev.next = my_next
        if my_next:
            my_next.prev = my_prev

        if n.key == self.tail.key:
            self._retreat_tail()

        self._add_as_head(n)

    def _retreat_tail(self):
        tail = None
        if self.tail:
            tail = self.tail
            new_tail = self.tail.prev
            if new_tail:
                new_tail.next = None
            self.tail.prev = None
            self.tail = new_tail
        return tail

    def _add_as_head(self, n):
        n.next = self.head
        n.prev = None

        if self.head:
            self.head.prev = n

        self.head = n

        if not self.tail:
            self.tail = self.head

    def print(self):
        buffer = ""
        node = self.head
        while node:
            buffer += str(node.key)
            buffer += " -> "
            node = node.next
        print(buffer)

        buffer = ""
        node = self.tail
        while node:
            buffer += str(node.key)
            buffer += " -> "
            node = node.prev
        print(buffer)


class LRUCache(object):
    def __init__(self, capacity):
        self.store = SimpleLinkedList(capacity)
        self.lookup = {}

    def put(self, key, val):
        if key not in self.lookup:
            n_removed = self.store.evict_last_if_full()
            if n_removed:
                del self.lookup[n_removed.key]

            n = Node(key, val)
            self.store.add_as_head(n)
            self.lookup[key] = n
        else:
            n = self.lookup[key]
            n.val = val
            self.store.move_to_head(n)

    def get(self, key):
        if key in lookup:
            n = self.lookup[key]
            self.store.move_to_head(n)
            return n.val

        return None

    def print(self):
        print([k for k, v in self.lookup.items()])
        self.store.print()


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        cache = LRUCache(3)
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        cache.put("k3", "v3")
        cache.put("k2", "v2")
        cache.put("k4", "v4")
        cache.put("k2", "v5")
        cache.put("k5", "v5")
        cache.put("k2", "v5")
        cache.put("k6", "v5")
        cache.put("k7", "v5")
        cache.put("k8", "v5")
        cache.put("k9", "v5")
        cache.put("k9", "v5")
        cache.put("k10", "v5")
        cache.put("k11", "v5")
        cache.put("k12", "v5")
        cache.print()


if __name__ == "__main__":
    unittest.main()
