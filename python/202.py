# 202. Happy Number
# https://leetcode.com/problems/happy-number/
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        happyDict = {}

        return self.checkHappy(n, happyDict)

    def checkHappy(self, n, happyDict):
        tmp = 0
        while (n > 0):
            tmp += pow(n % 10, 2)
            n = n / 10
        if tmp == 1:
            return True
        elif tmp in happyDict:
            return False
        else:
            happyDict[tmp] = 0
            return self.checkHappy(tmp, happyDict)