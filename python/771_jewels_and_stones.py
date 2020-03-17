# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        dic = dict()
        num = 0
        for elem in J:
            dic.setdefault(elem, 0)
        for elem in S:
            if elem in dic:
                num = num + 1
        dic.clear()
        return num