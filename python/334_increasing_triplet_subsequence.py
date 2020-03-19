# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums) < 3):
            return False
        i = None
        j = None
        for n in nums:
            if(i == None or i >= n):
                i = n
            elif(j == None or j >= n):
                j = n
            else:
                return True
        return False