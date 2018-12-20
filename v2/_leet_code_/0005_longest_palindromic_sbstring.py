class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        longest = 1
        start = end = 0
        for i in range(0, len(chars) - 1):
            c_max, c_st, c_end = self.longestFromCenter(chars, i, i)
            if c_max >= longest:
                longest = c_max
                start = c_st
                end = c_end
            c_max, c_st, c_end = self.longestFromCenter(chars, i, i + 1)
            if c_max >= longest:
                longest = c_max
                start = c_st
                end = c_end
        return s[start:end + 1]


    def longestFromCenter(self, text, l, r):
        size = start = end = 0
        while l >= 0 and r < len(text):
            if text[l] == text[r]:
                size, start, end = r - l + 1, l, r
                r += 1
                l -= 1
            else:
                break
        return (size, start, end)


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("b", s.longestPalindrome("abc"))
        self.assertEqual("bcb", s.longestPalindrome("abcabcbb"))
        self.assertEqual("bb", s.longestPalindrome("abcaecbb"))
        self.assertEqual("aa", s.longestPalindrome("aacdecbed"))
        self.assertEqual("bcb", s.longestPalindrome("abcaecbcb"))
        self.assertEqual("cac", s.longestPalindrome("acacdecbbd"))
        self.assertEqual("cbbc", s.longestPalindrome("abcabcbbc"))
        self.assertEqual("cbbc", s.longestPalindrome("cbbcabcab"))
        self.assertEqual("cbabc", s.longestPalindrome("cbabcabcab"))
        self.assertEqual("cbabc", s.longestPalindrome("abcaecbabc"))


if __name__ == '__main__':
    unittest.main()