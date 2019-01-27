class HitWindow:
    def __init__(self, timestamp, hits=1):
        self.timestamp = timestamp
        self.hits = hits

    def bump(self):
        self.hits += 1


class HitCounter:
    WSIZE = 300

    def __init__(self):
        self._hits = 0
        self.window = [None] * HitCounter.WSIZE
        self.start = 0
        self.count = 0

    def hit(self, timestamp):
        last_idx = self._last_idx()
        if self.count and self.window[last_idx].timestamp == timestamp:
            self.window[last_idx].bump()
        else:
            if self.count < HitCounter.WSIZE:
                self.count += 1
            else:
                self._hits -= self.window[self.start].hits
                self.start = (self.start + 1) % HitCounter.WSIZE
            self.window[self._last_idx()] = HitWindow(timestamp)

        self._hits += 1

    def getHits(self, timestamp):
        self._trim(timestamp)
        return self._hits

    def _trim(self, timestamp):
        def calc_idx(start, i):
            return (start + i) % HitCounter.WSIZE

        count = self.count
        start = self.start
        for i in range(count):
            idx = calc_idx(start, i)
            if self.window[idx].timestamp <= timestamp - HitCounter.WSIZE:
                self._hits -= self.window[idx].hits
                self.window[idx] = None
                self.count -= 1
                self.start = (self.start + 1) % HitCounter.WSIZE
            else:
                break

    def _last_idx(self):
        return (self.start + self.count - 1) % HitCounter.WSIZE


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        counter = HitCounter()

        counter.hit(1)
        counter.hit(2)
        counter.hit(3)

        self.assertEqual(3, counter.getHits(4))

        counter.hit(300)
        self.assertEqual(4, counter.getHits(300))
        self.assertEqual(3, counter.getHits(301))
        self.assertEqual(0, counter.getHits(3000))

    def test_2(self):
        counter = HitCounter()

        for i in range(300):
            counter.hit(i)

        self.assertEqual(0, counter.start)
        self.assertEqual(300, counter.count)
        self.assertEqual(299, counter._last_idx())
        self.assertEqual(300, counter.getHits(299))

        for i in range(300, 600):
            self.assertEqual(299, counter.getHits(i))
            counter.hit(i)
            self.assertEqual(300, counter.getHits(i))

    def test_3(self):
        counter = HitCounter()

        for i in range(400):
            counter.hit(i)

        self.assertEqual(100, counter.start)
        self.assertEqual(300, counter.count)
        self.assertEqual(99, counter._last_idx())
        self.assertEqual(300, counter.getHits(399))

    def test_4(self):
        counter = HitCounter()

        for i in range(300):
            counter.hit(i)
            counter.hit(i)

        self.assertEqual(0, counter.start)
        self.assertEqual(300, counter.count)
        self.assertEqual(299, counter._last_idx())
        self.assertEqual(600, counter.getHits(299))

        for i in range(300, 600):
            self.assertEqual(2 * 299, counter.getHits(i))
            counter.hit(i)
            counter.hit(i)
            self.assertEqual(600, counter.getHits(i))


if __name__ == "__main__":
    unittest.main()
