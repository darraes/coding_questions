class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def word_break(s, word_dict, start, lookup):
            if start == len(s):
                return True

            if start in lookup:
                return lookup[start]

            for i in range(start, len(s) + 1):
                if s[start:i] in word_dict:
                    if word_break(s, word_dict, i, lookup):
                        lookup[start] = True
                        return lookup[start]
                        
            lookup[start] = False
            return lookup[start]

        return word_break(s, wordDict, 0, {})


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(True, s.wordBreak("applepenapple", ["apple", "pen"]))
        self.assertEqual(True, s.wordBreak("leetcode", ["leet", "code"]))
        self.assertEqual(False, s.wordBreak("leetcod", ["leet", "code"]))
        self.assertEqual(False, s.wordBreak("leecode", ["leet", "code"]))
        self.assertEqual(
            False, s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
        )


if __name__ == "__main__":
    unittest.main()
