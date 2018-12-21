import sys

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        valley = sys.maxsize
        max_profit = 0
        for i in range(len(prices)):
            valley = min(valley, prices[i])
            max_profit = max(max_profit, prices[i] - valley)

        return max_profit


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        
        self.assertEqual(5, s.maxProfit([7,1,5,3,6,4]))
        self.assertEqual(39, s.maxProfit([7,1,5,3,6,40]))

if __name__ == "__main__":
    unittest.main()