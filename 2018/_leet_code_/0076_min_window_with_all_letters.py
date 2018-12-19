class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        targets = {}
        counts = {}
        for c in t:
            if c not in targets:
                targets[c] = 0    
            targets[c] += 1
            counts[c] = 0
        hits = 0

        max_left = max_right = None
        left = right = 0
        while right < len(s) or hits == len(targets):
            if hits != len(targets):
                if s[right] in counts:
                    counts[s[right]] += 1
                    if counts[s[right]] == targets[s[right]]:
                        hits += 1
                right += 1

            if hits == len(targets):
                if max_left is None or max_right - max_left > right - left:
                    max_left, max_right = left, right
                if s[left] in counts:
                    if counts[s[left]] == targets[s[left]]:
                        hits -= 1
                    counts[s[left]] -= 1
                left += 1

        if max_left is not None:
            return s[max_left:max_right]
        else:
            return ""


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("BANC", s.minWindow("ADOBECODEBANC", "ABC"))
        self.assertEqual("", s.minWindow("ADOBECODEBANC", "ZA"))
        self.assertEqual("ACB", s.minWindow("AAAAAAAAAAACB", "ABC"))
        self.assertEqual("C", s.minWindow("AAAAAAAAAAACB", "C"))
        self.assertEqual("DAAAAAAAAAACB", s.minWindow("DAAAAAAAAAACB", "DB"))
        self.assertEqual("", s.minWindow("a", "aa"))
        self.assertEqual("CAAAB", s.minWindow("DAAAAAAACAAAB", "AABC"))
        self.assertEqual("AACCCAAAB", s.minWindow("DAAAAAAACCCAAAB", "AAAAABC"))


if __name__ == "__main__":
    unittest.main()
