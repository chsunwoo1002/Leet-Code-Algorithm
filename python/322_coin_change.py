# 322. Coin Change
# https://leetcode.com/problems/coin-change/
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coinSum = [float('inf')] * (amount + 1)
        coinSum[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                coinSum[i] = min(coinSum[i], coinSum[i - coin] + 1)
        if (coinSum[amount] == float('inf')):
            return -1
        else:
            return coinSum[amount]
