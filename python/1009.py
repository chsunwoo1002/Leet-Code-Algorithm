# 1009. Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N is 0:
            return 1
        ans = 0
        binary = 0

        while N > 0:
            if N % 2 is 0:
                ans += pow(2, binary)
            N = N / 2
            binary += 1

        return ans