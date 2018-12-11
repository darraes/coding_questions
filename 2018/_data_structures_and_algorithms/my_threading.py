from collections import deque
from threading import Thread, RLock, Condition, Semaphore


class MPMCQueue(object):
    def __init__(self, max_size):
        self.buffer = deque(maxlen=max_size)
        self.max_size = max_size

        lock = RLock()
        self.not_full = Condition(lock)
        self.not_empty = Condition(lock)

    def put(self, task, blocking=True):
        self.not_full.acquire()

        while len(self.buffer) == self.max_size:
            if not blocking:
                return False

            self.not_full.wait()

        self.buffer.append(task)
        print("putting ", task)

        self.not_empty.notify()
        self.not_full.release()
        return True

    def get(self, blocking=True):
        self.not_empty.acquire()

        while len(self.buffer) == 0:
            if not blocking:
                return None

            self.not_empty.wait()

        task = self.buffer.popleft()
        print("getting ", task)
        self.not_full.notify()
        self.not_empty.release()
        return task


class MPMCSQueue(object):
    def __init__(self, max_size):
        self.buffer = deque(maxlen=max_size)
        self.max_size = max_size
        self.lock = RLock()
        self.used = Semaphore(value = 0)
        self.available = Semaphore(value = max_size)

    def put(self, task, blocking=True):
        if not self.available.acquire(blocking):
            return False

        self.lock.acquire()
        self.buffer.append(task)
        print("putting ", task)
        self.lock.release()

        self.used.release()
        return True

    def get(self, blocking=True):
        if not self.used.acquire(blocking):
            return None

        self.lock.acquire()
        task = self.buffer.popleft()
        self.lock.release()

        self.available.release()
        print("getting ", task)
        return task

###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_mpmc_1(self):
        mpmc = MPMCQueue(5)

        t1 = Thread(target=mpmc.put, args=(1,))
        t2 = Thread(target=mpmc.put, args=(2,))
        t3 = Thread(target=mpmc.put, args=(3,))
        t4 = Thread(target=mpmc.get)
        t5 = Thread(target=mpmc.get)
        t6 = Thread(target=mpmc.get)

        t4.start()
        t5.start()
        t6.start()
        t1.start()
        t2.start()
        t3.start()

    def test_mpmc_2(self):
        mpmc = MPMCSQueue(5)

        t1 = Thread(target=mpmc.put, args=(1,))
        t2 = Thread(target=mpmc.put, args=(2,))
        t3 = Thread(target=mpmc.put, args=(3,))
        t4 = Thread(target=mpmc.get)
        t5 = Thread(target=mpmc.get)
        t6 = Thread(target=mpmc.get)

        t4.start()
        t5.start()
        t6.start()
        t1.start()
        t2.start()
        t3.start()


if __name__ == "__main__":
    unittest.main()
