class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        digits = [0] * (len(num1) + len(num2))

        for i in reversed(range(len(num1))):
            p1 = len(num1) - i - 1
            p2 = p1 + 1
            for j in reversed(range(len(num2))):
                mul = int(num1[i]) * int(num2[j])
                digits[p1] += mul % 10
                digits[p2] += mul // 10
                if digits[p1] >= 10:
                    digits[p2] += digits[p1] // 10
                    digits[p1] %= 10

                p1 += 1
                p2 += 1

        digits.reverse()
        res = "".join([str(d) for d in digits])
        res = res.lstrip("0")

        return "0" if res == "" else res


###############################################################
import unittest
import sys


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("621", s.multiply("23", "27"))
        self.assertEqual("27", s.multiply("1", "27"))
        self.assertEqual("27", s.multiply("27", "1"))
        self.assertEqual("11407", s.multiply("671", "17"))
        self.assertEqual("0", s.multiply("0", "17"))
        self.assertEqual("0", s.multiply("0", "0"))
        self.assertEqual("1", s.multiply("1", "1"))


if __name__ == "__main__":
    unittest.main()
