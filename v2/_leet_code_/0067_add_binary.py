class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def convert(s):
            if s == 3:
                return 1, 1
            elif s == 2:
                return 0, 1
            else:
                return s, 0

        a = [int(n) for n in list(a)]
        a.reverse()

        b = [int(n) for n in list(b)]
        b.reverse()

        res = []
        carry = b_i = a_i = 0
        while b_i < len(b) or a_i < len(a) or carry:
            s = carry
            carry = 0

            if a_i < len(a):
                s += a[a_i]
                a_i += 1
            if b_i < len(b):
                s += b[b_i]
                b_i += 1

            r, carry = convert(s)
            res.append(r)

        return "".join([str(n) for n in reversed(res)])

###############################################################
import unittest
from tree_utils import TreeNode, pretty_print, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("100", s.addBinary(a="11", b="1"))
        self.assertEqual("1", s.addBinary(a="0", b="1"))
        self.assertEqual("10", s.addBinary(a="1", b="1"))
        self.assertEqual("11", s.addBinary(a="1", b="10"))
        self.assertEqual("10101", s.addBinary(a="1010", b="1011"))


if __name__ == "__main__":
    unittest.main()
