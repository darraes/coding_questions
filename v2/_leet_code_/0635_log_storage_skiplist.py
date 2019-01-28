from random import random


class SkipNode:
    def __init__(self, key, val, max_levels):
        self.key = key
        self.val = val
        self.next = [None] * max_levels


class SkipList:
    def __init__(self, max_levels, log_factor):
        self.max_levels = max_levels
        self.log_factor = log_factor
        self.level = 0
        self.head = SkipNode(0, "", self.max_levels)

    def random_level(self):
        level = 0
        while level < self.max_levels - 1 and random() < self.log_factor:
            level += 1
        return level

    def scan(self, start, end):
        current = self.head
        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < start:
                current = current.next[i]

        current = current.next[0]

        ans = []
        while current and current.key < end:
            ans.append(current.val)
            current = current.next[0]
        return ans

    def insert(self, key, val):
        current = self.head
        b_links = [self.head] * self.max_levels

        for i in range(self.level, -1, -1):
            while current.next[i] and current.next[i].key < key:
                current = current.next[i]
            b_links[i] = current

        current = current.next[0]

        if current and current.key == key:
            current.val = val
            return

        node = SkipNode(key, val, self.max_levels)
        nlevel = self.random_level()

        for i in range(nlevel + 1):
            node.next[i] = b_links[i].next[i]
            b_links[i].next[i] = node

        if nlevel > self.level:
            self.level = nlevel

    def display_list(self):
        head = self.head
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.next[lvl]
            while node != None:
                print(node.key, end=" ")
                node = node.next[lvl]
            print("")


class LogSystem:
    def __init__(self):
        self.storage = SkipList(5, 0.5)
        self.granularities = ["Year", "Month", "Day", "Hour", "Minute", "Second"]

    def put(self, val, timestamp):
        key = self.to_secs(timestamp)
        self.storage.insert(key, val)

    def retrieve(self, s, e, gra):
        start = self.to_secs(self.apply_granularity(s, gra))
        end = self.to_secs(self.apply_granularity(e, gra, 1))

        return self.storage.scan(start, end)

    def apply_granularity(self, t, gra, bump=0):
        parts = t.split(":")
        ignore = False
        for i in range(6):
            if ignore:
                parts[i] = "00"
            elif gra == self.granularities[i]:
                ignore = True
                parts[i] = str(int(parts[i]) + bump)

        return ":".join(parts)

    def to_secs(self, t):
        parts = [int(p) for p in t.split(":")]

        parts[1] = parts[1] - (0 if parts[1] == 0 else 1)
        parts[2] = parts[2] - (0 if parts[2] == 0 else 1)

        timestamp = 0
        timestamp += (parts[0] - 1999) * 12 * 31 * 24 * 60 * 60
        timestamp += parts[1] * 31 * 24 * 60 * 60
        timestamp += parts[2] * 24 * 60 * 60
        timestamp += parts[3] * 60 * 60
        timestamp += parts[4] * 60
        timestamp += parts[5]

        return timestamp


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        logdevice = LogSystem()

        self.assertTrue(
            logdevice.to_secs("2004:00:00:00:00:00")
            > logdevice.to_secs("2003:12:12:20:30:51")
        )

    def test_2(self):
        logdevice = LogSystem()
        logdevice.put(1, "2017:01:01:23:59:59")
        logdevice.put(2, "2017:01:01:22:59:59")
        logdevice.put(3, "2016:01:01:00:00:00")
        self.assertEqual(
            [3, 2, 1],
            logdevice.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"),
        )
        self.assertEqual(
            [2, 1],
            logdevice.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"),
        )

        logdevice = LogSystem()
        logdevice.put(1, "2017:01:01:23:59:59")
        logdevice.put(2, "2017:01:01:22:59:59")
        logdevice.put(3, "2016:01:01:00:00:00")
        self.assertEqual(
            [3, 2, 1],
            logdevice.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"),
        )
        self.assertEqual(
            [2, 1],
            logdevice.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"),
        )

    def test_3(self):
        logdevice = LogSystem()
        logdevice.put(1, "2005:01:05:22:16:15")
        logdevice.put(2, "2003:12:12:20:30:51")
        self.assertEqual(
            [],
            logdevice.retrieve("2005:07:10:17:43:43", "2007:02:18:10:22:52", "Month"),
        )
        logdevice.put(3, "2001:06:25:23:51:23")
        logdevice.put(4, "2004:10:25:13:49:48")
        logdevice.put(5, "2002:05:03:14:21:45")
        logdevice.put(6, "2004:10:04:21:49:49")
        self.assertEqual(
            [2, 6, 4, 1],
            logdevice.retrieve("2003:05:18:16:45:48", "2007:12:05:10:36:51", "Hour"),
        )

        logdevice.put(7, "2006:05:14:18:30:30")
        logdevice.put(8, "2003:04:02:22:12:41")
        logdevice.put(9, "2002:02:25:13:12:24")
        logdevice.put(10, "2005:01:17:23:36:39")
        logdevice.put(11, "2000:07:25:12:45:16")
        logdevice.put(12, "2001:08:12:16:35:55")
        logdevice.put(13, "2000:10:18:18:46:38")
        self.assertEqual(
            [6, 4, 1, 10],
            logdevice.retrieve("2004:09:23:19:31:46", "2005:10:27:16:51:21", "Year"),
        )


if __name__ == "__main__":
    unittest.main()
