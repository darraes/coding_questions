from random import random


class SkipNode:
    def __init__(self, key, val, max_level):
        self.key = key
        self.val = val
        self.next = [None] * (max_level + 1)


class SkipList:
    def __init__(self, max_level, log_factor):
        self.max_level = max_level
        self.log_factor = log_factor
        self.level = 0
        self.head = SkipNode(0, "", self.max_level)

    def random_level(self):
        level = 0
        while level < self.max_level and random() < self.log_factor:
            level += 1
        return level

    def insert(self, key, val):
        current = self.head
        b_links = [None] * (self.max_level + 1)

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]
            b_links[i] = current

        current = current.next[0]

        if current and current.key == key:
            current.val = val
            return

        nlevel = self.random_level()

        if nlevel > self.level:
            for i in range(self.level + 1, nlevel + 1):
                b_links[i] = self.head
            self.level = nlevel

        node = SkipNode(key, val, self.max_level)
        print(key, val)
        for i in range(nlevel + 1):
            node.next[i] = b_links[i].next[i]
            b_links[i].next[i] = node

        # Display skip list level wise

    def display_list(self):
        head = self.head
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.next[lvl]
            while node != None:
                print(node.key, end=" ")
                node = node.next[lvl]
            print("")


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        lst = SkipList(3, 0.5)
        lst.insert(3, "v123v")
        lst.insert(6, "v123v")
        lst.insert(7, "v123v")
        lst.insert(9, "v123v")
        lst.insert(12, "v123v")
        lst.insert(19, "v123v")
        lst.insert(17, "v123v")
        lst.insert(26, "v123v")
        lst.insert(21, "v123v")
        lst.insert(25, "v123v")
        lst.display_list()


if __name__ == "__main__":
    unittest.main()
