# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(0, len(s)):
            count += self.count_palindrominc(s, i)
        return count

    def count_palindrominc(self, text, i):
        count = 0
        s = e = i
        while s >= 0 and e < len(text):
            if text[s] != text[e]:
                break
            s -= 1
            e += 1
            count += 1

        s = i - 1
        e = i
        while s >= 0 and e < len(text):
            if text[s] != text[e]:
                break
            s -= 1
            e += 1
            count += 1

        return count


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(6, s.countSubstrings("aaa"))
        self.assertEqual(7, s.countSubstrings("babcc"))


if __name__ == "__main__":
    unittest.main()
