class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        number = str(x)

        s = 0
        e = len(number) - 1

        while s < e:
            if number[s] != number[e]:
                return False
            s += 1
            e -= 1
        return True


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertTrue(s.isPalindrome(121))
        self.assertTrue(s.isPalindrome(2))
        self.assertTrue(s.isPalindrome(1122211))
        self.assertFalse(s.isPalindrome(-121))
        self.assertFalse(s.isPalindrome(12))
        self.assertFalse(s.isPalindrome(222223))


if __name__ == '__main__':
    unittest.main()