# n = 4
# 1 + perm(2, 3, 4) = 6
# 2 + perm(1, 3, 4) = 6
# 3 + perm(1, 2, 4) = 6
# 4 + perm(1, 2, 3) = 6
#
# n = 3
# 1 + perm(2, 3) = 2
# 2 + perm(1, 3) = 2
# 3 + perm(1, 2) = 2
#

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorials = [0] * (n + 1)
        factorials[1] = 1
        for i in range(2, n + 1):
            factorials[i] = i * factorials[i - 1]

        res = []
        def kth_permutation(n, k, left):
            nonlocal factorials, res
            if k == 1:
                res.extend([str(n) for n in left])
                return

            idx = (k - 1) // factorials[n - 1]
            res.append(str(left[idx]))
            del left[idx]

            kth_permutation(n - 1, k - idx * factorials[n - 1], left)

        kth_permutation(n, k, [i for i in range(1, n + 1)])
        return "".join(res)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual("21", s.getPermutation(2, 2))
        self.assertEqual("12", s.getPermutation(2, 1))
        self.assertEqual("213", s.getPermutation(3, 3))
        self.assertEqual("2314", s.getPermutation(4, 9))
        self.assertEqual("4321", s.getPermutation(4, 24))
        self.assertEqual("1234", s.getPermutation(4, 1))


if __name__ == "__main__":
    unittest.main()