import threading
import time

class SpinLock(object):
    SPIN_CYCLES = 4000

    def __init__(self):
        self._state = 0
        self._lock = threading.Lock()
        self._owner_thread = 0
        return


    def acquire(self):
        attempts = 0
        while True:
            attempts += 1
            if self._compare_exchange(1, 0) == 0 \
              or self._owner_thread == threading.currentThread().ident:

                self._owner_thread = threading.currentThread().ident
                print "Acquired by {}".format(threading.currentThread().ident)
                return
            else:
                #If too many attempts, do something

                for i in range(SpinLock.SPIN_CYCLES):
                    pass


    def release(self):
        if self._compare_exchange(0, 1) == 1:
            print "Released by {}".format(threading.currentThread().ident)
            return
        else:
            raise "Wrong!!"


    def _compare_exchange(self, value, comparand):
        with self._lock:
            if self._state == comparand:
                old = self._state
                self._state = value
                return old
            return self._state

         
sp = SpinLock()
def test():
    sp.acquire()
    sp.acquire()
    time.sleep(0.05)
    sp.release()

t1 = threading.Thread(target = test)
t2 = threading.Thread(target = test)
t3 = threading.Thread(target = test)
t4 = threading.Thread(target = test)
t5 = threading.Thread(target = test)
t6 = threading.Thread(target = test)

t4.start()
t5.start()
t6.start()
t1.start()
t2.start()
t3.start()