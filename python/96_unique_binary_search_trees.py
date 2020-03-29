# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        treeMap = {}
        treeMap[0] = 1
        treeMap[1] = 1
        return self.findNumTrees(n, treeMap)

    def findNumTrees(self, n, treeMap):
        if n == 0:
            return treeMap[0]
        if n == 1:
            return treeMap[1]
        else:
            if n in treeMap:
                return treeMap[n]
            else:
                treeMap[n] = 0
                for i in range(n):
                    treeMap[n] += self.findNumTrees(i, treeMap) * self.findNumTrees(n - i - 1, treeMap)
                return treeMap[n]