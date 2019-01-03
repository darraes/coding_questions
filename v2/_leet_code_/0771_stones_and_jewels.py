class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(list(J))
        return len([s for s in list(S) if s in jewels])


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.numJewelsInStones("aA", "aAAbbbb"))
        self.assertEqual(0, s.numJewelsInStones("z", "ZZ"))


if __name__ == "__main__":
    unittest.main()
