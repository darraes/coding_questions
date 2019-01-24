class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def interleave(i1, i2):
            nonlocal memo, s1, s2, s3

            if i1 == len(s1) and i2 == len(s2):
                return True

            if (i1, i2) in memo:
                return memo[(i1, i2)]

            res = False

            if i1 < len(s1) and s1[i1] == s3[i1 + i2]:
                res |= interleave(i1 + 1, i2)

            if i2 < len(s2) and s2[i2] == s3[i1 + i2]:
                res |= interleave(i1, i2 + 1)

            memo[(i1, i2)] = res
            return res

        return interleave(0, 0)


################################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_positive(self):
        s = Solution()

        self.assertTrue(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
        self.assertFalse(s.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))


if __name__ == "__main__":
    unittest.main()
