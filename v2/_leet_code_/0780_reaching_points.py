class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx

        return False


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual(True, s.reachingPoints(sx=1, sy=1, tx=3, ty=5))

        self.assertEqual(False, s.reachingPoints(sx=1, sy=1, tx=2, ty=2))

        self.assertEqual(True, s.reachingPoints(sx=1, sy=1, tx=1, ty=1))


if __name__ == "__main__":
    unittest.main()
