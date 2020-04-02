# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [float('inf'), float('-inf')]
        self.findPosition(0, len(nums) - 1, ans, target, nums)
        if ans[0] == float('inf'):
            return [-1, -1]
        else:
            return ans

    def findPosition(self, left, right, ans, target, nums):
        if (right >= left):
            pivot = (left + right) / 2
            if nums[pivot] > target:
                self.findPosition(left, pivot - 1, ans, target, nums)
            elif nums[pivot] < target:
                self.findPosition(pivot + 1, right, ans, target, nums)
            else:
                ans[0] = min(pivot, ans[0])
                ans[1] = max(pivot, ans[1])
                self.findPosition(left, pivot - 1, ans, target, nums)
                self.findPosition(pivot + 1, right, ans, target, nums)
