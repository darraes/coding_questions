class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def _subsets(nums, i):
            if i == len(nums):
                return [[]]

            sub_ans = _subsets(nums, i + 1)
            ans = []
            for sub_ans in sub_ans:
                ans.append(sub_ans)
                ans.append([nums[i]] + sub_ans)

            return ans

        return _subsets(nums, 0)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(
            [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], s.subsets([1, 2, 3])
        )
        self.assertEqual(
            [[], [1]], s.subsets([1])
        )
        self.assertEqual(
            [[]], s.subsets([])
        )


if __name__ == "__main__":
    unittest.main()
