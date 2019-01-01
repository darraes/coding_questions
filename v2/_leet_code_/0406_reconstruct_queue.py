class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        tmp = sorted(people, key=lambda x: (-x[0], x[1]))
        ans = []
        for p in tmp:
            ans.insert(p[1], p)
        return ans


###############################################################
import unittest
import sys


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
            s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]),
        )


if __name__ == "__main__":
    unittest.main()
