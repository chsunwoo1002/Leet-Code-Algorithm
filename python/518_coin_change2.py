# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coinSum = [0] * (amount + 1)
        coinSum[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if (j >= i):
                    coinSum[j] += coinSum[j - i]
        return coinSum[amount]



