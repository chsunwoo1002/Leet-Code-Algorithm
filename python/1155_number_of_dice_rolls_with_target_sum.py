# 1155. Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution(object):
    def sumDice(self, d, f, target):
        if((d, target) in self.myList):
            return self.myList[(d, target)]
        if(d == 0 and target == 0):
            return 1
        if(d == 0 and target != 0):
            return 0
        ans = 0
        for i in range(1, f+1):
            ans += self.sumDice(d-1, f, target - i)
        self.myList[(d, target)] = ans
        return self.myList[(d, target)]

    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if(d == 0):
            return 0
        self.myList = dict()
        modul = 10**9 + 7
        return self.sumDice(d, f, target)%modul

