# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        global ans, lenList
        lenList = len(candidates)
        ans = []
        tmp = []

        self.findCombination(target, candidates, tmp, 0)

        return ans

    def findCombination(self, target, candidates, tmp, position):
        if target == 0:
            ans.append(tmp[:])
        elif target < 0:
            return
        else:
            for i in range(position, lenList):
                tmp.append(candidates[i])
                self.findCombination(target - candidates[i], candidates, tmp, i)
                tmp.pop()
