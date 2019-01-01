class Solution:
    def canPartition(self, nums):
        if len(nums) == 0:
            return False

        s = sum(nums)
        if s % 2 == 1:
            return False

        goal = s // 2

        def search(idx, target, memo):
            nonlocal nums, goal

            if idx == len(nums):
                return target == 0
            if nums[idx] > goal:
                return False

            if (idx, target) in memo:
                return memo[(idx, target)]

            if nums[idx] > target:
                memo[(idx, target)] = search(idx + 1, target, memo)
            elif nums[idx] == target:
                memo[(idx, target)] = True
            else:
                memo[(idx, target)] = search(
                    idx + 1, target - nums[idx], memo
                ) or search(idx + 1, target, memo)
            return memo[(idx, target)]

        return search(0, goal, {})

    def canPartition2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        def partition(idx, left, right):
            nonlocal nums

            if idx == len(nums):
                return sum(left) == sum(right)

            left.append(nums[idx])
            if partition(idx + 1, left, right):
                return True
            del left[-1]

            right.append(nums[idx])
            if partition(idx + 1, left, right):
                return True
            del right[-1]

            return False

        return partition(0, [], [])


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertTrue(s.canPartition([1, 5, 11, 5]))
        self.assertTrue(s.canPartition([1, 2, 9, 10]))

        self.assertFalse(s.canPartition([1, 2, 3, 5]))
        self.assertFalse(s.canPartition([15]))
        self.assertFalse(s.canPartition([]))
        self.assertTrue(
            s.canPartition(
                [
                    9,
                    67,
                    15,
                    64,
                    51,
                    53,
                    21,
                    1,
                    98,
                    84,
                    70,
                    53,
                    96,
                    90,
                    57,
                    39,
                    12,
                    21,
                    13,
                    19,
                    70,
                    2,
                    2,
                    58,
                    57,
                    59,
                    67,
                    83,
                    49,
                    86,
                    45,
                    53,
                    68,
                    57,
                    84,
                    87,
                    38,
                    97,
                    71,
                    72,
                    13,
                    57,
                    40,
                    100,
                    2,
                    19,
                    24,
                    90,
                    1,
                    45,
                    34,
                    34,
                    55,
                    97,
                    65,
                    73,
                    58,
                    23,
                    27,
                    1,
                    8,
                    6,
                    91,
                    72,
                    15,
                    3,
                    97,
                    30,
                    36,
                    44,
                    99,
                    19,
                    88,
                    63,
                    17,
                    57,
                    37,
                    39,
                    6,
                    69,
                    22,
                    55,
                    65,
                    89,
                    44,
                    94,
                    41,
                    17,
                    6,
                    12,
                    20,
                    31,
                    53,
                    80,
                    6,
                    24,
                    38,
                    45,
                    8,
                    24,
                ]
            )
        )
        self.assertTrue(
            s.canPartition(
                [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                ]
            )
        )


if __name__ == "__main__":
    unittest.main()
