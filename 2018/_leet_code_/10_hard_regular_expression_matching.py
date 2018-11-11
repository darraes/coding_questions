class State(object):
    ANY = "."     


class CharState(State):
    def __init__(self, char, state_id):
        self.state_idx = state_id
        self.char = char

    def execute(self, input_text, cursor):
        transitions = []
        if cursor >= len(input_text):
            return transitions

        if self.char == State.ANY or input_text[cursor] == self.char:
            transitions.append((self.state_idx + 1, cursor + 1))
        return transitions


class StarState(State):
    def __init__(self, char, state_id):
        self.state_idx = state_id
        self.char = char

    def execute(self, input_text, cursor):
        transitions = []
        if cursor >= len(input_text):
            return transitions

        transitions.append((self.state_idx + 1, cursor))
        if self.char == State.ANY or input_text[cursor] == self.char:
            transitions.append((self.state_idx, cursor + 1))
            transitions.append((self.state_idx + 1, cursor + 1))

        return transitions



class StateMachine(object):
    def __init__(self):
        self.states = []

    def from_regex(self, regex):
        self.states = []
        idx = i = 0

        while i <len(regex):
            char = regex[i]
            if i < len(regex) - 1 and regex[i + 1] == "*":
                self.states.append(StarState(char, idx))
                i += 2
            else:
                self.states.append(CharState(char, idx))
                i += 1
            idx += 1

    def execute(self, input_text):
        return self._execute_impl(input_text, 0, 0)

    def _execute_impl(self, input_text, cursor, state_idx):
        # print(state_idx, cursor)

        if state_idx >= len(self.states) and cursor >= len(input_text):
            return True
        if state_idx >= len(self.states) or cursor >= len(input_text):
            return False

        transitions = self.states[state_idx].execute(input_text, cursor)
        for next_state_id, next_cursor in transitions:
            res = self._execute_impl(input_text, next_cursor, next_state_id)
            if res:
                return True
        return False


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = StateMachine()
        s.from_regex("a*b*.")
        self.assertTrue(s.execute("abc"))
        self.assertTrue(s.execute("c"))
        self.assertTrue(s.execute("aabbbc"))
        self.assertFalse(s.execute("aabbbcd"))
        self.assertTrue(s.execute("a"))
        self.assertFalse(s.execute("bca"))

    def test_2(self):
        s = StateMachine()
        s.from_regex("a")
        self.assertFalse(s.execute("abc"))
        self.assertFalse(s.execute("c"))
        self.assertFalse(s.execute("aabbbc"))
        self.assertFalse(s.execute("aabbbcd"))
        self.assertTrue(s.execute("a"))
        self.assertFalse(s.execute("bca"))

    def test_3(self):
        s = StateMachine()
        s.from_regex(".*")
        self.assertTrue(s.execute("abc"))
        self.assertTrue(s.execute("c"))
        self.assertTrue(s.execute("aabbbc"))
        self.assertTrue(s.execute("aabbbcd"))
        self.assertTrue(s.execute("a"))
        self.assertTrue(s.execute("bca"))


if __name__ == '__main__':
    unittest.main()













               
        