from collections import deque
from threading import Condition


class MPMCQueue(object):
    def __init__(self, max_size):
        self.buffer = deque(maxlen = max_size)
        self.size = 0
        self.cfull = Condition()
        self.cempty = Condition()


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_mpmc_1(self):
        mpmc = MPMCQueue(5)


if __name__ == "__main__":
    unittest.main()