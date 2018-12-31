class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        buy = [0] * len(prices)
        sell = [0] * len(prices)

        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], prices[i] + buy[i - 1])

        return sell[-1]


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(3, s.maxProfit([1,2,3,0,2]))
        self.assertEqual(0, s.maxProfit([1]))
        self.assertEqual(2, s.maxProfit([1, 3]))
        self.assertEqual(3, s.maxProfit([1, 3, 4]))
        self.assertEqual(3, s.maxProfit([1, 4, 3]))



if __name__ == "__main__":
    unittest.main()