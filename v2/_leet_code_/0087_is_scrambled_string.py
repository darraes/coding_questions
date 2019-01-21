class Solution:
    def are_anagrams(self, w1, w2):
        return sorted(w1) == sorted(w2)

    def isScramble(self, s1, s2):
        if not self.are_anagrams(s1, s2):
            return False

        if s1 == s2:
            return True

        for i in range(1, len(s1)):
            if (
                # No scrambled happened on this level
                self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
            ) or (
                # A scramble happened in this level
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])
            ):
                return True
        return False


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertTrue(s.isScramble(s1="great", s2="eatgr"))
        self.assertTrue(s.isScramble(s1="great", s2="rgeat"))
        self.assertTrue(s.isScramble(s1="a", s2="a"))
        self.assertTrue(s.isScramble(s1="ab", s2="ba"))

        self.assertFalse(s.isScramble(s1="abcde", s2="caebd"))
        self.assertFalse(s.isScramble(s1="a", s2="b"))


if __name__ == "__main__":
    unittest.main()
