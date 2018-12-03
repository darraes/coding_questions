from collections import deque


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        stack = deque()
        score = {}
        for idx, char in enumerate(list(s)):
            if char == "(":
                stack.append((idx))
            elif len(stack) > 0:
                start = stack.pop()
                current_length = idx - start + 1

                if start - 1 in score:
                    current_length += score[start - 1]

                score[idx] = current_length
                max_length = max(max_length, current_length)

        return max_length


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(4, s.longestValidParentheses(")()())"))
        self.assertEqual(2, s.longestValidParentheses("(()"))
        self.assertEqual(2, s.longestValidParentheses("()"))
        self.assertEqual(0, s.longestValidParentheses("("))
        self.assertEqual(0, s.longestValidParentheses(")"))
        self.assertEqual(8, s.longestValidParentheses("(())(())"))
        self.assertEqual(8, s.longestValidParentheses("()()()()"))
        self.assertEqual(4, s.longestValidParentheses("(()))(())"))


if __name__ == "__main__":
    unittest.main()
