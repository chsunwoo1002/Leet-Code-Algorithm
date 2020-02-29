# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curMax = 0
        left = 0
        right = len(height) - 1
        while (left < right):
            width = right - left
            h = min(height[left], height[right])
            tmp = (right - left) * h
            curMax = max(curMax, tmp)
            if (height[left] > height[right]):
                right -= 1
            else:
                left += 1
        return curMax