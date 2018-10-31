# Amazon Phone Screen #1
from collections import deque
import threading

class IntegerDispatcher(object):
    def __init__(self):
        self._data = 0
        self._producer = threading.Semaphore(1, 1)
        self._consumer = threading.Semaphore(0, 1)

    """Puts data to be consumed"""
    def put(self, data):
        self._producer.acquire()
        try:
            self._data = data
            print "put {} ".format(data)
            self._consumer.release()
        except:
            self._producer.release()

    """Consumes the data"""
    def get(self):
        self._consumer.acquire()
        try:
            # not really needed, but for clarity
            data = self._data
            self._data = 0

            self._producer.release()
            print "get {} ".format(data)
            return data
        except:
            self._consumer.release()


class Dispatcher(object):
    def __init__(self):
        self._data = deque()
        self._control = threading.Condition()

    """Puts data to be consumed"""
    def put(self, data):
        self._control.acquire()
        try:
            self._data.append(data)
            print "put {} ".format(data)
        finally:
            self._control.notify()
            self._control.release()            

    """Puts data to be consumed"""
    def get(self):
        self._control.acquire()
        try:
            data = 0
            while True:
                if len(self._data) > 0:
                    data = self._data.popleft()
                    print "get {} ".format(data)
                    break;
                self._control.wait()
            return data
        finally:
            self._control.release()


dispatcher = Dispatcher()

t1 = threading.Thread(target = dispatcher.put, args = (1,))
t2 = threading.Thread(target = dispatcher.put, args = (2,))
t3 = threading.Thread(target = dispatcher.put, args = (3,))
t4 = threading.Thread(target = dispatcher.get)
t5 = threading.Thread(target = dispatcher.get)
t6 = threading.Thread(target = dispatcher.get)

t4.start()
t5.start()
t6.start()
t1.start()
t2.start()
t3.start()

g = threading.Semaphore(0)
g.release()
g.release()
g.release()
g.release()




        