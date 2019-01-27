from threading import Thread, RLock, Condition, Semaphore, currentThread, Barrier
from time import sleep


class KeepOrder:
    def __init__(self):
        self._lock = RLock()
        self._status = 1

        self._ready_for_2 = Condition(self._lock)
        self._ready_for_3 = Condition(self._lock)

        self.calls = []

    def first(self):
        self._lock.acquire()

        self.calls.append(1)

        self._status = 2
        self._ready_for_2.notify()

        self._lock.release()

    def second(self):
        self._lock.acquire()

        if self._status < 2:
            self._ready_for_2.wait()

        self.calls.append(2)

        self._status = 3
        self._ready_for_3.notify()

        self._lock.release()

    def third(self):
        self._lock.acquire()

        if self._status < 3:
            self._ready_for_3.wait()

        self.calls.append(3)

        self._lock.release()


class KeepOrder2:
    def __init__(self):
        self._ready_for_1 = Semaphore(1)
        self._ready_for_2 = Semaphore(0)
        self._ready_for_3 = Semaphore(0)

        self.calls = []

    def first(self):
        self._ready_for_1.acquire()
        self.calls.append(1)
        self._ready_for_2.release()

    def second(self):
        self._ready_for_2.acquire()
        self.calls.append(2)
        self._ready_for_3.release()

    def third(self):
        self._ready_for_3.acquire()
        self.calls.append(3)
        self._ready_for_1.release()


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_ko_1(self):
        ko = KeepOrder()

        t1 = Thread(target=ko.first)
        t2 = Thread(target=ko.second)
        t3 = Thread(target=ko.third)

        t3.start()
        t2.start()
        t1.start()

        sleep(0.1)

        self.assertEqual([1, 2, 3], ko.calls)

    def test_ko_2(self):
        ko = KeepOrder2()

        t1 = Thread(target=ko.first)
        t2 = Thread(target=ko.second)
        t3 = Thread(target=ko.third)

        t3.start()
        t2.start()
        t1.start()

        sleep(0.1)

        self.assertEqual([1, 2, 3], ko.calls)


if __name__ == "__main__":
    unittest.main()
