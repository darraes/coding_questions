class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        conversion_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        progression = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        result = ""
        cur = 0
        while num > 0:
            if num >= progression[cur]:
                result += conversion_map[progression[cur]]
                num -= progression[cur]
            else:
                cur += 1

        return result


####### =============== TESTS ===============
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("III", s.intToRoman(3))
        self.assertEqual("IV", s.intToRoman(4))
        self.assertEqual("IX", s.intToRoman(9))
        self.assertEqual("LVIII", s.intToRoman(58))
        self.assertEqual("MCMXCIV", s.intToRoman(1994))
        self.assertEqual("MCDXCIV", s.intToRoman(1494))


if __name__ == "__main__":
    unittest.main()
