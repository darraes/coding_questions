#########################################################################
# Given a class Stream with the below interface, implement a class called
# MultiStream to abstract the reading from multiple streams and provide
# a "sequential" read of the data as all streams could be one.

#  class Stream:
#      def read(self, count) -> List[int]:
#          Implementation omitted

#  class MultiStream:
#      def read(self, count) -> List[int]:
#          TODO
#
#      def add_stream(self, stream: Stream) -> str:
#          TODO
#
#      def remove_stream(self, id: str):
#          TODO
#
# PS: Alternatively, you can pass the output buffer as input of the read()
# methods and have the read return the number of bytes read.
#########################################################################


from doubly_linked_list import SentinelDoublyList
from typing import List
from uuid import uuid4


class Stream:
    def __init__(self, data):
        self.data = data

    def read(self, count) -> List[int]:
        res = self.data[:count]
        self.data = self.data[count:]
        return res


class MultiStream:
    class Node:
        def __init__(self, id, stream):
            self.id = id
            self.stream = stream

    def __init__(self):
        self._lookup = {}
        self._streams = SentinelDoublyList()

    def add_stream(self, stream: Stream) -> str:
        id = str(uuid4())

        node = self._streams.append(MultiStream.Node(id, stream))
        self._lookup[id] = node
        return id

    def remove_stream(self, id: str):
        if id not in self._lookup or self._streams.head().id == id:
            return False

        node = self._lookup[id]
        del self._lookup[id]
        self._streams.unlink(node)

        return True

    def read(self, count) -> List[int]:
        buffer = [0] * count
        cursor, to_read = 0, count

        def move_to_buffer(bts):
            nonlocal cursor, buffer
            for b in bts:
                buffer[cursor] = b
                cursor += 1

        while to_read > 0 and self._streams.head() is not None:
            stream = self._streams.head().stream
            bytes_read = stream.read(to_read)

            to_read -= len(bytes_read)
            move_to_buffer(bytes_read)

            if to_read:
                self._streams.unlink(self._streams.head())

        return buffer[:cursor]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_add_read(self):
        s1 = Stream("daniel")
        s2 = Stream("arraes")
        s3 = Stream("pereira")

        ms = MultiStream()
        ms.add_stream(s1)
        ms.add_stream(s2)
        ms.add_stream(s3)

        self.assertEqual(list("dani"), ms.read(4))
        self.assertEqual(list("elar"), ms.read(4))
        self.assertEqual(list("raes"), ms.read(4))
        self.assertEqual(list("pere"), ms.read(4))
        self.assertEqual(list("ira"), ms.read(4))
        self.assertEqual([], ms.read(4))

    def test_remove_future(self):
        s1 = Stream("daniel")
        s2 = Stream("arraes")
        s3 = Stream("pereira")

        ms = MultiStream()
        ms.add_stream(s1)
        id2 = ms.add_stream(s2)
        ms.add_stream(s3)

        self.assertEqual(list("dani"), ms.read(4))

        ms.remove_stream(id2)

        self.assertEqual(list("elpe"), ms.read(4))
        self.assertEqual(list("reir"), ms.read(4))
        self.assertEqual(list("a"), ms.read(4))
        self.assertEqual([], ms.read(4))

    def test_remove_current(self):
        s1 = Stream("daniel")
        s2 = Stream("arraes")
        s3 = Stream("pereira")

        ms = MultiStream()
        ms.add_stream(s1)
        id2 = ms.add_stream(s2)
        ms.add_stream(s3)

        self.assertEqual(list("dani"), ms.read(4))
        self.assertEqual(list("elar"), ms.read(4))
        ms.remove_stream(id2)
        self.assertEqual(list("raes"), ms.read(4))
        self.assertEqual(list("pere"), ms.read(4))
        self.assertEqual(list("ira"), ms.read(4))
        self.assertEqual([], ms.read(4))


if __name__ == "__main__":
    unittest.main()
