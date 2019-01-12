from collections import deque

class Solution:
    def __init__(self):
        self.memory = deque()

    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""]*4
            l = read4(buf4)
            self.memory.extend(buf4)
            curr = min(len(self.memory), n-idx)
            for i in xrange(curr):
                buf[idx] = self.memory.popleft()
                idx+=1
            if curr == 0:
                break 
        return idx