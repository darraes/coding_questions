class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.longest_unique_substring_v2(s)

    def longest_unique_substring(self, text):
        res = 0
        b_window = e_window = 0
        window = set()

        chars = list(text)

        while e_window < len(chars):
            if chars[e_window] not in window:
                window.add(chars[e_window])
                e_window += 1
                res = max(res, e_window - b_window)
            else:
                window.remove(chars[b_window])
                b_window += 1

        return res


    def longest_unique_substring_v2(self, text):
        res = 0
        b_window = e_window = 0
        window = {}

        chars = list(text)

        while e_window < len(chars):
            if chars[e_window] not in window \
                    or window[chars[e_window]] < b_window:
                window[chars[e_window]] = e_window
                e_window += 1
                res = max(res, e_window - b_window)
            else:
                b_window = window[chars[e_window]] + 1
                window[chars[e_window]] = e_window
                e_window += 1

        return res


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.longest_unique_substring("abcabcbb"))
        self.assertEqual(1, s.longest_unique_substring("a"))
        self.assertEqual(1, s.longest_unique_substring("aa"))
        self.assertEqual(0, s.longest_unique_substring(""))
        self.assertEqual(10, s.longest_unique_substring("abcdefghij"))
        self.assertEqual(2, s.longest_unique_substring("aaaai"))

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
