class Solution:
    def numberOfArithmeticSlices(self, A):
        return self.approach_2(A)

    def approach_1(self, A):
        count = 0
        for i in range(len(A) - 1):
            d = A[i + 1] - A[i]
            for j in range(i + 2, len(A)):
                if d == A[j] - A[j - 1]:
                    count += 1
                else:
                    break

        return count

    def approach_2(self, A):
        res = 0

        def slices(A, i):
            nonlocal res
            if i < 2:
                return 0

            tmp = 0
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                tmp = 1 + slices(A, i - 1)
                res += tmp
            else:
                slices(A, i - 1)
            return tmp

        slices(A, len(A) - 1)
        return res


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.numberOfArithmeticSlices([1, 2, 3, 4]))
        self.assertEqual(4, s.numberOfArithmeticSlices([1, 2, 3, 4, 7, 10]))


if __name__ == "__main__":
    unittest.main(exit=False)
