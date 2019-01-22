class Solution:
    def findPairs(self, nums, k):
        """
        a - b = k => a = k + b
          or
        a - b = -k => a = -k + b
        """
        if k < 0:
            return 0

        def make_pair(a, b):
            return (a, b) if a < b else (b, a)

        ans = set()
        complements = set()

        for i in range(len(nums)):
            if k + nums[i] in complements:
                ans.add(make_pair(nums[i], k + nums[i]))
            if -k + nums[i] in complements:
                ans.add(make_pair(nums[i], -k + nums[i]))
            complements.add(nums[i])

        return len(ans)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(2, s.findPairs([3, 1, 4, 1, 5], k=2))
        self.assertEqual(4, s.findPairs([1, 2, 3, 4, 5], k=1))
        self.assertEqual(1, s.findPairs([1, 3, 1, 5, 4], k=0))

        self.assertEqual(2, s.findPairs([-3, -1, -4, -1, -5], k=2))
        self.assertEqual(1, s.findPairs([-1, -3, -1, -5, -4], k=0))

        self.assertEqual(1, s.findPairs([1, 1, 1, 2, 1], 1))


if __name__ == "__main__":
    unittest.main()
