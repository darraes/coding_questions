class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.cursor_i = 0
        self.cursor_j = 0
        self.wait_on_next()

    def wait_on_next(self):
        while self.cursor_i < len(self.vec2d) and len(self.vec2d[self.cursor_i]) == 0:
            self.cursor_i += 1

    def next(self):
        """
        :rtype: int
        """
        res = self.vec2d[self.cursor_i][self.cursor_j]
        self.cursor_j += 1

        if self.cursor_j == len(self.vec2d[self.cursor_i]):
            self.cursor_j = 0
            self.cursor_i += 1
            self.wait_on_next()

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cursor_i < len(self.vec2d) - 1:
            return True
        if self.cursor_i == len(self.vec2d) - 1:
            return self.cursor_j < len(self.vec2d[self.cursor_i])
        return False


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        ans = []
        v = Vector2D([[1, 2], [3], [4, 5, 6]])
        while v.hasNext():
            ans.append(v.next())
        self.assertEqual([1, 2, 3, 4, 5, 6], ans)

        ans = []
        v = Vector2D([[1, 2], [], [4, 5, 6]])
        while v.hasNext():
            ans.append(v.next())
        self.assertEqual([1, 2, 4, 5, 6], ans)

        ans = []
        v = Vector2D([[], [1, 2], [4, 5, 6], []])
        while v.hasNext():
            ans.append(v.next())
        self.assertEqual([1, 2, 4, 5, 6], ans)


if __name__ == "__main__":
    unittest.main()
