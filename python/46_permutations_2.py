# 46. Permutations 2
# https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        oneList = []
        wholeList = []
        visited = [False] * len(nums)
        self.backTrack(oneList, wholeList, visited, nums)
        return wholeList

    def backTrack(self, oneList, wholeList, visited, nums):
        if len(oneList) == len(nums):
            wholeList.append(oneList[:])
        else:
            for index, value in enumerate(nums):
                if visited[index] is False:
                    visited[index] = True
                    oneList.append(value)
                    self.backTrack(oneList, wholeList, visited, nums)
                    oneList.pop()
                    visited[index] = False

