# 46. Permutations
# https://leetcode.com/problems/permutations/
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        oneList = []
        wholeList = []
        self.backTracking(oneList, wholeList, nums)

        return wholeList

    def backTracking(self, oneList, wholeList, nums):
        if (len(oneList) == len(nums)):
            wholeList.append(oneList[:])
            return
        else:
            for i in nums:
                if i not in oneList:
                    oneList.append(i)
                    self.backTracking(oneList, wholeList, nums)
                    oneList.remove(i)

