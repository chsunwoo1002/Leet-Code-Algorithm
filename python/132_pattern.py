# 456. 132 Pattern
# https://leetcode.com/problems/132-pattern/
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = float('-inf')
        index, top = len(nums) - 1, len(nums)

        while index >= 0:
            if nums[index] < last: return True

            while top < len(nums) and nums[index] > nums[top]:
                last = nums[top]
                top += 1
            top -= 1
            nums[top] = nums[index]
            index -= 1

        return False