class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conversion_map = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        res = 0
        for idx in range(len(s)):
            if idx < len(s) - 1 and \
                    conversion_map[s[idx]] < conversion_map[s[idx + 1]]:
                res -= conversion_map[s[idx]]
            else:
                res += conversion_map[s[idx]]
            idx += 1
        return res


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.romanToInt("III"))
        self.assertEqual(4, s.romanToInt("IV"))
        self.assertEqual(9, s.romanToInt("IX"))
        self.assertEqual(58, s.romanToInt("LVIII"))
        self.assertEqual(1994, s.romanToInt("MCMXCIV"))
        self.assertEqual(1494, s.romanToInt("MCDXCIV"))


if __name__ == "__main__":
    unittest.main()
