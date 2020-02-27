# 525 Contiguous Array
# https://leetcode.com/problems/contiguous-array/
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = max_len = 0
        myMap = {0: -1}
        for index, element in enumerate(nums):
            if element is 1:
                count += 1
            else:
                count -= 1
            if count in myMap:
                max_len = max(max_len, index - myMap.get(count))
            else:
                myMap[count] = index

        return max_len