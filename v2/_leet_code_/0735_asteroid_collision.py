class Solution:
    def moving_left(self, n):
        return n < 0

    def moving_right(self, n):
        return n > 0

    def asteroidCollision(self, asteroids):
        if len(asteroids) == 0:
            return []

        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            if self.moving_right(asteroids[i]):
                stack.append(asteroids[i])
            else:
                current_survived = True
                while len(stack) > 0 and self.moving_right(stack[-1]):
                    if abs(asteroids[i]) > abs(stack[-1]):
                        stack.pop()
                    elif abs(asteroids[i]) < abs(stack[-1]):
                        current_survived = False
                        break
                    else:
                        stack.pop()
                        current_survived = False
                        break
                if current_survived:
                    stack.append(asteroids[i])
        return stack


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([-2], s.asteroidCollision([1, 1, 1, -2]))
        self.assertEqual([2], s.asteroidCollision([2, -1, -1, -1]))
        self.assertEqual([5, 10], s.asteroidCollision([5, 10, -5]))
        self.assertEqual([], s.asteroidCollision([]))
        self.assertEqual([], s.asteroidCollision([8, -8]))
        self.assertEqual([], s.asteroidCollision([8, 8, -8, -8]))
        self.assertEqual([10], s.asteroidCollision([10, 2, -5]))
        self.assertEqual([-2, -1, 1, 2], s.asteroidCollision([-2, -1, 1, 2]))


if __name__ == "__main__":
    unittest.main()


class OldSolution:
    def collide(self, asteroids, l, r):
        continue_idx = l
        if abs(asteroids[l]) > abs(asteroids[r]):
            # Keeping the left
            asteroids = asteroids[:r] + asteroids[r + 1 :]
        elif abs(asteroids[l]) < abs(asteroids[r]):
            # Keeping the right
            asteroids = asteroids[:l] + asteroids[r:]
        else:
            # remove both
            asteroids = asteroids[:l] + asteroids[r + 1 :]
            continue_idx = l - 1
        return asteroids, continue_idx

    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        i = 0
        while i < len(asteroids):
            if (
                i < len(asteroids) - 1
                and self.moving_right(asteroids[i])
                and self.moving_left(asteroids[i + 1])
            ):
                asteroids, i = self.collide(asteroids, i, i + 1)
            elif (
                i > 0
                and self.moving_left(asteroids[i])
                and self.moving_right(asteroids[i - 1])
            ):
                asteroids, i = self.collide(asteroids, i - 1, i)
            else:
                i += 1
        return asteroids
