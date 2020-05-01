from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]

            seen[num] = idx

        return [-1, -1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual([0, 1], s.twoSum([2, 7, 11, 15], 9))
        self.assertEqual([0, 3], s.twoSum([2, 7, 11, 15], 17))


if __name__ == "__main__":
    unittest.main()