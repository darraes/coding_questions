class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        while x > 0 or y > 0:
            if x & 1 != y & 1:
                distance +=1

            if x:
                x = x >> 1
            if y:
                y = y >> 1

        return distance


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(2, s.hammingDistance(1, 4))
        self.assertEqual(0, s.hammingDistance(1, 1))
        self.assertEqual(0, s.hammingDistance(0, 0))
        self.assertEqual(0, s.hammingDistance(7, 7))

if __name__ == "__main__":
    unittest.main()
