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
        transitions.append((self.state_idx + 1, cursor))

        if cursor >= len(input_text):
            return transitions

        if self.char == State.ANY or input_text[cursor] == self.char:
            # transitions.append((self.state_idx + 1, cursor + 1))
            transitions.append((self.state_idx, cursor + 1))

        return transitions


class StateMachine(object):
    def __init__(self):
        self.states = []

    def from_regex(self, regex):
        self.states = []
        idx = i = 0

        while i < len(regex):
            char = regex[i]
            if i < len(regex) - 1 and regex[i + 1] == "*":
                self.states.append(StarState(char, idx))
                i += 2
            else:
                self.states.append(CharState(char, idx))
                i += 1
            idx += 1

    def execute(self, input_text):
        return self._execute_impl(input_text, 0, 0, {})

    def _execute_impl(self, input_text, cursor, state_idx, memo):
        # print(state_idx, cursor)
        if (cursor, state_idx) in memo:
            return memo[(cursor, state_idx)]

        if state_idx >= len(self.states) and cursor >= len(input_text):
            return True
        if state_idx >= len(self.states):
            return False

        transitions = self.states[state_idx].execute(input_text, cursor)
        for next_state_id, next_cursor in transitions:
            res = self._execute_impl(input_text, next_cursor, next_state_id, memo)
            memo[(next_cursor, next_state_id)] = res
            if res:
                return True
        return False


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        state_machine = StateMachine()
        state_machine.from_regex(p)
        return state_machine.execute(s)


class Solution:
    def isMatch(self, s, p):
        memo = {}

        def dp(i, j):
            nonlocal s, p, memo

            if i == len(s) and j == len(p):
                return True
            if j >= len(p):
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            is_match = i < len(s) and p[j] in [".", s[i]]
            if j < len(p) - 1 and p[j + 1] == "*":
                memo[(i, j)] = dp(i, j + 2) or is_match and dp(i + 1, j)
            else:
                memo[(i, j)] = is_match and dp(i + 1, j + 1)

            return memo[(i, j)]

        return dp(0, 0)


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

        s = Solution()
        self.assertTrue(s.isMatch2("abc", "a*b*."))
        self.assertTrue(s.isMatch2("c", "a*b*."))
        self.assertTrue(s.isMatch2("aabbbc", "a*b*."))
        self.assertFalse(s.isMatch2("aabbbcd", "a*b*."))
        self.assertTrue(s.isMatch2("a", "a*b*."))
        self.assertFalse(s.isMatch2("bca", "a*b*."))

    def test_2(self):
        s = StateMachine()
        s.from_regex("a")
        self.assertFalse(s.execute("abc"))
        self.assertFalse(s.execute("c"))
        self.assertFalse(s.execute("aabbbc"))
        self.assertFalse(s.execute("aabbbcd"))
        self.assertTrue(s.execute("a"))
        self.assertFalse(s.execute("bca"))

        s = Solution()
        self.assertFalse(s.isMatch2("abc", "a"))
        self.assertFalse(s.isMatch2("c", "a"))
        self.assertFalse(s.isMatch2("aabbbc", "a"))
        self.assertFalse(s.isMatch2("aabbbcd", "a"))
        self.assertTrue(s.isMatch2("a", "a"))
        self.assertFalse(s.isMatch2("bca", "a"))

    def test_3(self):
        s = StateMachine()
        s.from_regex(".*")
        self.assertTrue(s.execute("abc"))
        self.assertTrue(s.execute("c"))
        self.assertTrue(s.execute("aabbbc"))
        self.assertTrue(s.execute("aabbbcd"))
        self.assertTrue(s.execute("a"))
        self.assertTrue(s.execute("bca"))

        s = Solution()
        self.assertTrue(s.isMatch2("abc", ".*"))
        self.assertTrue(s.isMatch2("c", ".*"))
        self.assertTrue(s.isMatch2("aabbbc", ".*"))
        self.assertTrue(s.isMatch2("aabbbcd", ".*"))
        self.assertTrue(s.isMatch2("a", ".*"))
        self.assertTrue(s.isMatch2("bca", ".*"))

    def test_4(self):
        s = StateMachine()
        s.from_regex("a*")
        self.assertFalse(s.execute("abc"))
        self.assertFalse(s.execute("c"))
        self.assertFalse(s.execute("aabbbc"))
        self.assertFalse(s.execute("aabbbcd"))
        self.assertTrue(s.execute("a"))
        self.assertTrue(s.execute("aa"))
        self.assertTrue(s.execute("aaa"))
        self.assertFalse(s.execute("bca"))

        s = Solution()
        self.assertFalse(s.isMatch2("abc", "a*"))
        self.assertFalse(s.isMatch2("c", "a*"))
        self.assertFalse(s.isMatch2("aabbbc", "a*"))
        self.assertFalse(s.isMatch2("aabbbcd", "a*"))
        self.assertTrue(s.isMatch2("a", "a*"))
        self.assertTrue(s.isMatch2("aa", "a*"))
        self.assertTrue(s.isMatch2("aaa", "a*"))
        self.assertFalse(s.isMatch2("bca", "a*"))

    def test_5(self):
        s = StateMachine()
        s.from_regex("mis*is*p*.")
        self.assertFalse(s.execute("mississippi"))

        s = Solution()
        self.assertFalse(s.isMatch2("mississippi", "mis*is*p*."))

    def test_6(self):
        s = StateMachine()
        s.from_regex("ab*")
        self.assertTrue(s.execute("a"))

        s = Solution()
        self.assertTrue(s.isMatch2("a", "ab*"))


if __name__ == "__main__":
    unittest.main()
