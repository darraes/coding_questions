from threading import RLock, Condition, ThreadPool, Thread
from heapq import heappush, heappop
from collections import namedtuple
from time import time

###########################################################
###########################################################
# IMPORTANT: This code doesn't run. This is just a concept
###########################################################
###########################################################


class Action:
    def execute():
        pass


ScheduledAction = namedtuple("ScheduledAction", ["action", "timestamp"])


class Scheduler:
    def __init__(self):
        self.runner = ThreadPool(24)  # Number of cores
        self.loop = Thread(self.run)
        self.lock = RLock()
        self.ready = Condition(self.lock)
        self.queue = []
        self.idle_lock = RLock()
        self.idle_queue = []
        self._shutdown = False

        self.loop.start()

    def shutdown(self):
        self._shutdown = True

    def defer_action(self, action: Action, defer_secs: int):
        self.idle_lock.aquire()
        self.idle_queue.append(ScheduledAction(time() + defer_secs, action))
        self.idle_lock.release()

        self.ready.notify()

    def run(self):
        def drain_idle_queue():
            self.idle_lock.aquire()
            # in CPP we can do a shared_ptr swap to be able to unlock with O(1)
            for n in self.idle_queue:
                heappush(self.queue, n)

            self.idle_queue = []
            self.idle_lock.release()

        while not self._shutdown:
            self.lock.aquire()

            drain_idle_queue()

            while self.queue and self.queue[0].timestamp <= time():
                self.runner.run(heappop(self.queue).action)

            drain_idle_queue()

            if self.queue:
                self.ready.wait_for(timeout=self.queue[0].timestamp - time())
            else:
                self.ready.wait()

            self.lock.release()

