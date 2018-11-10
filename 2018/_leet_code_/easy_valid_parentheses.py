# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closer = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for p in s:
            if p in closer:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                elif p != closer[stack.pop()]:
                    return False
        return len(stack) == 0


####### =============== TESTS =============== 
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertTrue(s.isValid("()"))
        self.assertTrue(s.isValid("()[]{}"))
        self.assertTrue(s.isValid("{[]}"))
        self.assertTrue(s.isValid("({[[]]})"))

        self.assertFalse(s.isValid("(]"))
        self.assertFalse(s.isValid("([)]"))
        self.assertFalse(s.isValid("("))
        self.assertFalse(s.isValid("]"))
        self.assertFalse(s.isValid("({[[]])})"))


if __name__ == '__main__':
    unittest.main()