class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] < amount + 1 else -1

    def coinChangeRec2(self, coins, amount):
        def _coinChangeRec2(coins, amount, lookup):
            if amount == 0:
                return 0
            if amount in lookup:
                return lookup[amount]

            ans = 2 ** 32 - 1
            for c in coins:
                if c <= amount:
                    ans = min(ans, 1 + _coinChangeRec2(coins, amount - c, lookup))

            lookup[amount] = ans
            return ans

        ans = _coinChangeRec2(coins, amount, {})
        return ans if ans != 2 ** 32 - 1 else -1

    def coinChangeRec(self, coins, amount):
        def _coinChangeRec(coins, amount, c_idx, lookup):
            if amount == 0:
                return 0
            if amount < 0 or c_idx == len(coins):
                return 2 ** 32 - 1
            if (c_idx, amount) in lookup:
                return lookup[(c_idx, amount)]

            ans = 2 ** 32 - 1
            cur_coin_count = 0
            while True:
                ans = min(
                    ans,
                    _coinChangeRec(
                        coins, amount - cur_coin_count * coins[c_idx], c_idx + 1, lookup
                    )
                    + cur_coin_count,
                )
                cur_coin_count += 1

                if cur_coin_count * coins[c_idx] > amount:
                    break

            lookup[(c_idx, amount)] = ans
            return ans

        ans = _coinChangeRec(coins, amount, 0, {})
        return ans if ans != 2 ** 32 - 1 else -1


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.coinChange([1, 2, 5], 11))
        self.assertEqual(4, s.coinChange([2, 5], 11))
        self.assertEqual(-1, s.coinChange([3, 5], 7))
        self.assertEqual(-1, s.coinChange([2], 7))
        self.assertEqual(7, s.coinChange([1], 7))
        self.assertEqual(16, s.coinChange([461, 307, 4, 97, 352, 446, 479, 243], 7265))

        self.assertEqual(3, s.coinChangeRec([1, 2, 5], 11))
        self.assertEqual(4, s.coinChangeRec([2, 5], 11))
        self.assertEqual(-1, s.coinChangeRec([3, 5], 7))
        self.assertEqual(-1, s.coinChangeRec([2], 7))
        self.assertEqual(7, s.coinChangeRec([1], 7))
        self.assertEqual(
            16, s.coinChangeRec([461, 307, 4, 97, 352, 446, 479, 243], 7265)
        )

        self.assertEqual(3, s.coinChangeRec2([1, 2, 5], 11))
        self.assertEqual(4, s.coinChangeRec2([2, 5], 11))
        self.assertEqual(-1, s.coinChangeRec2([3, 5], 7))
        self.assertEqual(-1, s.coinChangeRec2([2], 7))
        self.assertEqual(7, s.coinChangeRec2([1], 7))
        self.assertEqual(
            16, s.coinChangeRec2([461, 307, 4, 97, 352, 446, 479, 243], 7265)
        )


if __name__ == "__main__":
    unittest.main()
