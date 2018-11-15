class Solution:
    def myAtoi(self, _str):
        """
        :type str: str
        :rtype: int
        """
        if not _str:
            return 0

        _str = _str.lstrip()

        signs = ["-", "+"]
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        max_int = 2**31-1
        min_int = -2**31

        if not _str or (_str[0] not in signs and _str[0] not in digits):
            return 0

        idx = 0
        factor = 1
        if _str[0] in signs:
            if _str[0] == "-":
                factor = -1
            idx += 1

        result = 0
        while idx < len(_str) and _str[idx] in digits:
            result *= 10
            result += int(_str[idx])

            cur = factor * result
            if cur < min_int:
                return min_int
            if cur > max_int:
                return max_int

            idx += 1


        return factor * result




###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(42, s.myAtoi("42"))
        self.assertEqual(-42, s.myAtoi("    -42"))
        self.assertEqual(4193, s.myAtoi("4193 with words"))
        self.assertEqual(419, s.myAtoi(" 419 3 with words"))
        self.assertEqual(0, s.myAtoi("words and 987"))
        self.assertEqual(0, s.myAtoi(" "))
        self.assertEqual(0, s.myAtoi(""))
        self.assertEqual(0, s.myAtoi(None))
        self.assertEqual(-2147483648, s.myAtoi("-91283472332"))
        self.assertEqual(2147483647, s.myAtoi("91283472332"))
        self.assertEqual(-2147483648, s.myAtoi("-2147483648"))
        self.assertEqual(2147483647, s.myAtoi("2147483647"))
        self.assertEqual(-2147483647, s.myAtoi("-2147483647"))
        self.assertEqual(2147483646, s.myAtoi("2147483646"))


if __name__ == '__main__':
    unittest.main()