# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        profit = 0
        base = prices[0]
        for index in range(len(prices)):
            if base > prices[index]:
                base = prices[index]
            else:
                profit += prices[index] - base
                base = prices[index]
        return profit