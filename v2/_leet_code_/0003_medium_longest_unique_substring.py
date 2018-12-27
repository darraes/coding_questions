class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.longest_unique_substring(s)

    def longest_unique_substring(self, text):
        res = 0
        b_window = e_window = 0
        window = {}

        chars = list(text)

        while e_window < len(chars):
            if chars[e_window] not in window \
                    or window[chars[e_window]] < b_window:
                res = max(res, e_window - b_window + 1)
            else:
                b_window = window[chars[e_window]] + 1
            window[chars[e_window]] = e_window
            e_window += 1

        return res


###############################################################
import unittest

class TestFunctions(unittest.TestCase):

    def test_2(self):
        s = Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, s.lengthOfLongestSubstring("a"))
        self.assertEqual(1, s.lengthOfLongestSubstring("aa"))
        self.assertEqual(0, s.lengthOfLongestSubstring(""))
        self.assertEqual(10, s.lengthOfLongestSubstring("abcdefghij"))
        self.assertEqual(2, s.lengthOfLongestSubstring("aaaai"))
        self.assertEqual(2, s.lengthOfLongestSubstring("iaaaa"))
        self.assertEqual(5, s.lengthOfLongestSubstring("tmmzuxt"))


if __name__ == '__main__':
    unittest.main()
