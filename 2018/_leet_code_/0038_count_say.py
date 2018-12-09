class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(n - 1):
            let, temp, count = s[0], "", 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s


###############################################################


import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("1211", s.countAndSay(4))



if __name__ == "__main__":
    unittest.main()