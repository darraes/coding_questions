class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        s = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if s < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True

        memo = {}

        def guaranteed_victory(nums, desiredTotal):
            nonlocal memo
            if nums[-1] >= desiredTotal:
                return True

            key = tuple(nums)
            if key in memo:
                return memo[key]

            ans = False
            for idx, c in enumerate(nums):
                if not guaranteed_victory(
                    nums[:idx] + nums[idx + 1 :], desiredTotal - c
                ):
                    ans = True
                    break

            memo[key] = ans
            return memo[key]

        return guaranteed_victory(
            [x for x in range(1, maxChoosableInteger + 1)], desiredTotal
        )


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(False, s.canIWin(10, 11))
        self.assertEqual(True, s.canIWin(4, 6))
        self.assertEqual(False, s.canIWin(5, 50))


if __name__ == "__main__":
    unittest.main(exit=False)

