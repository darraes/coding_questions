from collections import deque
from threading import Thread, RLock, Condition, Semaphore, currentThread, Barrier
from time import sleep


class MPMCQueue(object):
    def __init__(self, max_size):
        self.buffer = deque(maxlen=max_size)
        self.max_size = max_size

        self.lock = RLock()
        self.not_full = Condition(self.lock)
        self.not_empty = Condition(self.lock)

    def put(self, task, blocking=True):
        self.lock.acquire()

        while len(self.buffer) == self.max_size:
            if not blocking:
                return False
            self.not_full.wait()

        self.buffer.append(task)
        print("putting ", task)
        self.not_empty.notify()

        self.lock.release()
        return True

    def get(self, blocking=True):
        self.lock.acquire()

        while len(self.buffer) == 0:
            if not blocking:
                return None
            self.not_empty.wait()

        task = self.buffer.popleft()
        print("getting ", task)
        self.not_full.notify()

        self.lock.release()
        return task


class MPMCSQueue(object):
    def __init__(self, max_size):
        self.buffer = deque(maxlen=max_size)
        self.max_size = max_size
        self.lock = RLock()
        self.ready_to_read = Semaphore(value=0)
        self.available_slots = Semaphore(value=max_size)

    def put(self, task, blocking=True):
        if not self.available_slots.acquire(blocking):
            return False

        self.lock.acquire()
        self.buffer.append(task)
        print("putting ", task)
        self.lock.release()

        self.ready_to_read.release()
        return True

    def get(self, blocking=True):
        if not self.ready_to_read.acquire(blocking):
            return None

        self.lock.acquire()
        task = self.buffer.popleft()
        self.lock.release()

        self.available_slots.release()
        print("getting ", task)
        return task


class SpinLock(object):
    SPIN_CYCLES = 4000

    def __init__(self):
        self.cs = RLock()
        self.flag = 0
        self._owner_thread = -1

    def acquire(self):
        kFree = 0
        while True:
            if (
                self.compare_exchange(val=1, comparand=kFree) == kFree
                or self._owner_thread == currentThread().ident
            ):
                self._owner_thread = currentThread().ident
                print("Acquired by {}".format(self._owner_thread))
                return

            for _ in range(SpinLock.SPIN_CYCLES):
                pass

    def release(self):
        if self._owner_thread == currentThread().ident:
            if self.compare_exchange(val=0, comparand=1) == 1:
                print("Released by {}".format(self._owner_thread))

    def compare_exchange(self, val, comparand):
        with self.cs:
            previous = self.flag
            if self.flag == comparand:
                self.flag = val

            return previous


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_mpmc_1(self):
        mpmc = MPMCQueue(2)

        t1 = Thread(target=mpmc.put, args=(1,))
        t2 = Thread(target=mpmc.put, args=(2,))
        t3 = Thread(target=mpmc.put, args=(3,))
        t4 = Thread(target=mpmc.get)
        t5 = Thread(target=mpmc.get)
        t6 = Thread(target=mpmc.get)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

    def test_mpmc_2(self):
        mpmc = MPMCSQueue(2)

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

    def test_spinlock(self):
        spin_lock = SpinLock()
        barrier = Barrier(6)

        def sl_test():
            nonlocal spin_lock, barrier
            barrier.wait()
            spin_lock.acquire()
            sleep(0.05)
            spin_lock.release()

        t1 = Thread(target=sl_test)
        t2 = Thread(target=sl_test)
        t3 = Thread(target=sl_test)
        t4 = Thread(target=sl_test)
        t5 = Thread(target=sl_test)
        t6 = Thread(target=sl_test)

        t4.start()
        t5.start()
        t6.start()
        t1.start()
        t2.start()
        t3.start()


if __name__ == "__main__":
    unittest.main()
