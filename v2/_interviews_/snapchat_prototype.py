from collections import deque
from time import time


class SnapQueue:
    def __init__(self, user_id):
        self.user_id = user_id
        self.list = ddlist()
        self.lookup = {}

    def post(self, id, content):
        node = self.list.append((id, content))
        self.lookup[id] = node

    def has_new(self, watched):
        # return list unwached ids

    def get_nonwatched_ids(self, watched):
        # return list unwached ids

    def earlist(self):
        # return id at the head of the queue


class Snapchat:
    def __init__(self):
        self.user_queues = {0: SnapQueue(0), 1: SnapQueue(1), 2: SnapQueue(2)}
        self.followerDB = {0: [1], 1: [0, 2]}
        self.state = {(0, 1, id): 0,}

    def post(self, user_id, content):
        if user_id not in self.user_queues:
            raise "TODO"

        self.user_queues[user_id].post(time(), content)

    def search(self, user_id):
        result = []

        # get all people that I follow
        followees = self.followerDB[user_id]

        for f_id in followees:
            fo_queue = self.user_queues[f_id]
            earlist = fo_queue.earlist()
            watched = self.state.scan((user_id, f_id, earlist))
            if fo_queue.has_new(watched):
                to_watch_ids = fo_queue.get_nonwatched_ids(watched)
                for to_watch in to_watch_ids:
                    result.append((to_watch, f_id, ...))

        return rank(result)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        pass


if __name__ == "__main__":
    unittest.main()
