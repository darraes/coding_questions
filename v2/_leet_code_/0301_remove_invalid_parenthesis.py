class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.remove(s, ans, 0, 0, "(", ")")
        return ans

    def remove(self, s, ans, last_i, last_j, opener, closer):
        score = 0
        for i in range(last_i, len(s)):
            if s[i] == opener:
                score += 1
            if s[i] == closer:
                score -= 1
            if score >= 0:
                continue

            for j in range(last_j, i + 1):
                if s[j] == closer and (j == last_j or s[j - 1] != closer):
                    self.remove(s[:j] + s[j + 1 :], ans, i, j, opener, closer)
            return

        s_reversed = "".join(reversed(list(s)))
        if opener == "(":
            self.remove(s_reversed, ans, 0, 0, closer, opener)
        else:
            ans.append(s_reversed)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(["(())()", "()()()"], s.removeInvalidParentheses("()())()"))
        self.assertEqual(["(a())()", "(a)()()"], s.removeInvalidParentheses("(a)())()"))
        self.assertEqual([""], s.removeInvalidParentheses(")("))


if __name__ == "__main__":
    unittest.main()
