class DoubleLinkedList:
    def __init__(self, node_builder):
        self.builder = node_builder
        self.head = self.builder(None, None)
        self.tail = self.builder(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def true_head(self):
        return self.head.next

    def true_tail(self):
        return self.tail.prev

    def append(self, n):
        ptail = self.tail.prev

        ptail.next = n
        n.prev = ptail

        n.next = self.tail
        self.tail.prev = n

        self.size += 1
        return n

    def appendleft(self, n):
        phead = self.head.next

        self.head.next = n
        n.prev = self.head

        n.next = phead
        phead.prev = n

        self.size += 1
        return n

    def appendbefore(self, n, next):
        prev = next.prev

        prev.next = n
        n.prev = prev

        n.next = next
        next.prev = n

        self.size += 1
        return n

    def pop(self):
        self.size -= 1
        return self.unlink(self.tail.prev).val

    def popleft(self):
        self.size -= 1
        return self.unlink(self.head.next).val

    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def print(self):
        self.print_f()
        self.print_b()

    def print_f(self):
        res = ""

        buf = ""
        node = self.true_head()
        while node != self.tail:
            buf += str(node) + "->"
            node = node.next
        print("F:", buf)
        return "F:" + buf

    def print_b(self):
        buf = ""
        node = self.true_tail()
        while node != self.head:
            buf += str(node) + "->"
            node = node.prev
        print("B:", buf)
        return "B:" + buf


class CacheNode:
    def __init__(self, key, val, freq_node):
        self.key = key
        self.val = val
        self.freq_node = freq_node
        self.next = None
        self.prev = None

    def __str__(self):
        return "({}, {})".format(self.key, self.val)


class FrequencyNode:
    def __init__(self, f):
        self.f = f
        self.clist = DoubleLinkedList(lambda k, v: CacheNode(None, None, None))
        self.next = None
        self.prev = None

    def __str__(self):
        return "({})".format(self.f)


class LFUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache_map = {}
        self.frequencies = DoubleLinkedList(lambda k, v: FrequencyNode(v))

    def put(self, key, val):
        if len(self.cache_map) == self.cap and key not in self.cache_map:
            self._evict_lfu()

        self._update(key, val)

    def get(self, key):
        if key not in self.cache_map:
            return None

        cnode = self.cache_map[key]
        v = cnode.val
        self._update(key, v)

        return v

    def _evict_lfu(self):
        fnode = self.frequencies.true_head()
        cnode = fnode.clist.popleft()
        del self.cache_map[cnode.key]

        if self.frequencies.size == 0:
            self.frequencies.unlink(fnode)

    def _update(self, key, val):
        if key in self.cache_map:
            cnode = self.cache_map[key]
            cnode.val = val
            fnode = cnode.freq_node

            f = fnode.f + 1
            fnext = fnode.next

            fnode.clist.unlink(cnode)
            if fnode.clist.size == 0:
                self.frequencies.unlink(fnode)

            if f == fnext.f:
                fnext.clist.appendleft(cnode)
            else:
                fnode = self.frequencies.appendbefore(FrequencyNode(f), fnext)
                fnode.clist.appendleft(cnode)
        else:
            fnode = FrequencyNode(1)
            if self.frequencies.true_head().f == 1:
                fnode = self.frequencies.true_head()
            else:
                self.frequencies.appendleft(fnode)

            cnode = CacheNode(key, val, fnode)
            fnode.clist.append(cnode)
            self.cache_map[key] = cnode

    def print_cache(self):
        print(self.cache_map)

        buf = ""
        node = self.frequencies.true_head()
        while node != self.frequencies.tail:
            print("Freq:", node.f)
            node.clist.print_f()
            node = node.next


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        print("==============")
        cache = LFUCache(5)
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        cache.put("k3", "v3")
        cache.put("k4", "v4")
        cache.put("k5", "v5")
        cache.put("k2", "v2")
        cache.put("k3", "v3")
        cache.print_cache()

    def test_2(self):
        print("==============")
        l = DoubleLinkedList(lambda k, v: CacheNode(None, None, None))

        l.append(CacheNode(1, 1, None))
        n3 = l.append(CacheNode(3, 3, None))
        l.append(CacheNode(4, 4, None))
        l.appendleft(CacheNode(0, 0, None))
        l.appendbefore(CacheNode(2, 2, None), n3)

        self.assertEqual("F:(0, 0)->(1, 1)->(2, 2)->(3, 3)->(4, 4)->", l.print_f())
        self.assertEqual("B:(4, 4)->(3, 3)->(2, 2)->(1, 1)->(0, 0)->", l.print_b())

        l.unlink(n3)
        self.assertEqual("F:(0, 0)->(1, 1)->(2, 2)->(4, 4)->", l.print_f())
        self.assertEqual("B:(4, 4)->(2, 2)->(1, 1)->(0, 0)->", l.print_b())

        l.pop()
        l.popleft()

        self.assertEqual("F:(1, 1)->(2, 2)->", l.print_f())
        self.assertEqual("B:(2, 2)->(1, 1)->", l.print_b())


if __name__ == "__main__":
    unittest.main()
