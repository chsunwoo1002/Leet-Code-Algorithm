# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = {}
        return self.countWays(n, count)

    def countWays(self, n, count):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if n in count:
                return count[n]
            else:
                count[n] = self.countWays(n - 2, count) + self.countWays(n - 1, count)
                return count[n]