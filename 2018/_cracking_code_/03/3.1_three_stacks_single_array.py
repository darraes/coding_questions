class StackTrio(object):
    class State:
        def __init__(self, base, size):
            self.base = base
            self.current = base
            self.size = size

    def __init__(self, size):
        self.store = [None] * (3 * size)
        self.max_size = size
        self.states = [
                        StackTrio.State(0, size),
                        StackTrio.State(size, size),
                        StackTrio.State(size * 2, size)
                      ]

    def push(self, s_id, element):
        if s_id >= len(self.states):
            raise "Invalid Stack"

        state = self.states[s_id]
        if state.current < state.base + state.size:
            self.store[state.current] = element
            state.current += 1
        else:
            raise "Full Stack"

    def pop(self, s_id):
        if s_id >= len(self.states):
            raise "Invalid Statck"

        element = None
        state = self.states[s_id]
        if state.current > state.base:
            state.current -= 1
            element = self.store[state.current]
            self.store[state.current] = None
        else:
            raise "Empty Stack"

        return element



###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = StackTrio(3)
        s.push(0, 0)
        s.push(1, 10)
        s.push(2, 100)

        self.assertEqual(0, s.pop(0))
        self.assertEqual(10, s.pop(1))
        self.assertEqual(100, s.pop(2))

        s.push(0, 0)
        s.push(1, 10)
        s.push(2, 100)
        s.push(0, 1)
        s.push(1, 11)
        s.push(2, 101)

        self.assertEqual(1, s.pop(0))
        self.assertEqual(11, s.pop(1))
        self.assertEqual(101, s.pop(2))
        self.assertEqual(0, s.pop(0))
        self.assertEqual(10, s.pop(1))
        self.assertEqual(100, s.pop(2))

        s.push(0, 0)
        s.push(1, 10)
        s.push(2, 100)
        s.push(0, 1)
        s.push(1, 11)
        s.push(2, 101)
        s.push(0, 2)
        s.push(1, 12)
        s.push(2, 102)

        self.assertEqual(2, s.pop(0))
        self.assertEqual(12, s.pop(1))
        self.assertEqual(102, s.pop(2))
        self.assertEqual(1, s.pop(0))
        self.assertEqual(11, s.pop(1))
        self.assertEqual(101, s.pop(2))
        self.assertEqual(0, s.pop(0))
        self.assertEqual(10, s.pop(1))
        self.assertEqual(100, s.pop(2))


if __name__ == '__main__':
    unittest.main()