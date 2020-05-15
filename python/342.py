# 342. Power of Four
# https://leetcode.com/problems/power-of-four/
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        return log(num, 4) % 1 == 0