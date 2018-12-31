# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        ans = []
        i = 0

        s = [c for c in s]
        multiplier = 0
        text = []

        while i < len(s):
            if "0" <= s[i] <= "9":
                multiplier *= 10
                multiplier += int(s[i])
            elif s[i] == "[":
                stack.append((text, multiplier))
                multiplier = 0
                text = []
            elif s[i] == "]":
                prev_text, mul = stack.pop()
                text = prev_text + (mul * text)

                if len(stack) == 0:
                    ans += text
                    text = []
            else:
                text += s[i]
            i += 1
        ans += text

        return "".join(ans)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("abcabccdcdcdef", s.decodeString("2[abc]3[cd]ef"))
        self.assertEqual("accaccacc", s.decodeString("3[a2[c]]"))
        self.assertEqual("abcabccdcdcdef", s.decodeString("2[abc]3[cd]ef"))
        self.assertEqual("ffaccaccacc", s.decodeString("ff3[a2[c]]"))
        self.assertEqual("aaaaaaaaaa", s.decodeString("10[a]"))
        self.assertEqual("aaaaaaaaaaa", s.decodeString("11[a]"))
        self.assertEqual("aaaaaaaa", s.decodeString("2[2[2[a]]]"))


if __name__ == "__main__":
    unittest.main()
