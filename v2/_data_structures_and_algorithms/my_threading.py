from collections import deque
from threading import Thread, RLock, Condition, Semaphore, currentThread, Barrier
from time import sleep


class RWLock:
    def __init__(self):
        self._lock = RLock()
        self._condition = Condition(self._lock)
        self._readers = 0
        self._write = False

    def acquire_read(self):
        self._lock.acquire()

        while self._write:
            self._condition.wait()
        self._readers += 1

        self._lock.release()

    def release_read(self):
        self._lock.acquire()

        self._readers -= 1
        if self._readers == 0:
            self._condition.notify_all()

        self._lock.release()

    def acquire_write(self):
        self._lock.acquire()

        while self._write:
            self._condition.wait()

        self._write = True
        while self._readers > 0:
            self._condition.wait()

        self._lock.release()

    def release_write(self):
        self._lock.acquire()

        self._condition.notify_all()
        self._write = False

        self._lock.release()


class MPMCQueue:
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
                return

            for _ in range(SpinLock.SPIN_CYCLES):
                pass

    def release(self):
        if self._owner_thread == currentThread().ident:
            if not self.compare_exchange(val=0, comparand=1) == 1:
                raise "Trying to release an unacquired lock"
        else:
            raise "Trying to release an unacquired lock"

    def compare_exchange(self, val, comparand):
        with self.cs:
            previous = self.flag
            if self.flag == comparand:
                self.flag = val

            return previous


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_rwlock_1(self):
        counter = 0
        kThreads = 50
        barrier = Barrier(2 * kThreads)
        rwlock = RWLock()
        simultaneuos_reads = 0
        max_simultaneuos_reads = 0

        def unsafe_read():
            nonlocal counter, barrier, rwlock, simultaneuos_reads, max_simultaneuos_reads
            barrier.wait()
            rwlock.acquire_read()
            simultaneuos_reads += 1
            sleep(0.0001)
            max_simultaneuos_reads = max(max_simultaneuos_reads, simultaneuos_reads)
            simultaneuos_reads -= 1
            rwlock.release_read()

        def unsafe_write():
            nonlocal counter, barrier, rwlock
            barrier.wait()
            rwlock.acquire_write()
            before = counter
            sleep(0.0002)
            counter = before + 1
            rwlock.release_write()

        tasks = []
        for _ in range(kThreads):
            tasks.append(Thread(target=unsafe_write))
            tasks.append(Thread(target=unsafe_read))

        for t in tasks:
            t.start()

        for t in tasks:
            t.join()

        self.assertEqual(kThreads, counter)
        self.assertTrue(max_simultaneuos_reads > 1)

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

        for t in [t1, t2, t3, t4, t5, t6]:
            t.join()

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

        for t in [t1, t2, t3, t4, t5, t6]:
            t.join()

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

        for t in [t1, t2, t3, t4, t5, t6]:
            t.join()


if __name__ == "__main__":
    unittest.main(exit=False)
