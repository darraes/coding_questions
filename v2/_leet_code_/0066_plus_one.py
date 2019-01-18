class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()

        carry = 1
        idx = 0

        while carry and idx < len(digits):
            digits[idx] += carry
            if digits[idx] >= 10:
                digits[idx] %= 10
            else:
                carry = 0
            idx += 1

        if carry:
            digits.append(1)

        digits.reverse()
        return digits


###############################################################
import unittest
from tree_utils import TreeNode, pretty_print, deserialize


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([1, 2, 4], s.plusOne([1, 2, 3]))
        self.assertEqual([1, 2, 4, 0], s.plusOne([1, 2, 3, 9]))
        self.assertEqual([2, 0, 0], s.plusOne([1, 9, 9]))
        self.assertEqual([1, 0], s.plusOne([9]))


if __name__ == "__main__":
    unittest.main()
