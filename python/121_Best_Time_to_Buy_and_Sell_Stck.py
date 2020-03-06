# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(prices == []):
            return 0
        maxProfit = 0
        base = prices[0]
        for index in range(len(prices)):
            if base > prices[index]:
                base = prices[index]
            else:
                if maxProfit < prices[index] - base:
                    maxProfit = prices[index]-base
        return maxProfit