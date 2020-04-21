# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        mapNum = {}
        for i in arr:
            mapNum[i] = mapNum.get(i, 0) + 1
        if len(set(mapNum.values())) == len(mapNum):
            return True
        else:
            return False