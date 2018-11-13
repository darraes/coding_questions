class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0:
            return ""
        if numRows == 1:
            return s

        sbuffer = []
        for x in range(numRows):
            sbuffer.append([])

        i = n = 0
        while i < len(s):
            while i < len(s) and n < numRows:
                sbuffer[n].append(s[i])
                n += 1
                i += 1

            n -= 2
            while i < len(s) and n >= 0:
                sbuffer[n].append(s[i])
                n -= 1
                i += 1
            n += 2

        result = ""
        for line in sbuffer:
            result += "".join(line)

        return result


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("PAHNAPLSIIGYIR", 
                          s.convert(s = "PAYPALISHIRING", numRows = 3))
        self.assertEqual("PINALSIGYAHRPI", 
                          s.convert(s = "PAYPALISHIRING", numRows = 4))
        self.assertEqual("AAAABBBB", 
                          s.convert(s = "ABABABAB", numRows = 2))
        self.assertEqual("PAYPALISHIRING", 
                          s.convert(s = "PAYPALISHIRING", numRows = 1))


if __name__ == '__main__':
    unittest.main()