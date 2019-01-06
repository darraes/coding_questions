class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        

###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([5, 10], s.asteroidCollision([5, 10, -5]))
        self.assertEqual([], s.asteroidCollision([8, -8]))
        self.assertEqual([10], s.asteroidCollision([10, 2, -5]))
        self.assertEqual([-2, -1, 1, 2], s.asteroidCollision([-2, -1, 1, 2]))