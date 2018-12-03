class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:(len(needle) + i)] == needle:
                return i

        return -1


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(2, s.strStr("hello", "ll"))
        self.assertEqual(0, s.strStr("hello", "he"))
        self.assertEqual(4, s.strStr("hello", "o"))
        self.assertEqual(-1, s.strStr("hello", "a"))
        self.assertEqual(0, s.strStr("hello", ""))


if __name__ == "__main__":
    unittest.main()
