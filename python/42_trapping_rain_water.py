# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total = 0
        if (len(height) <= 2):
            return 0
        left = 0
        right = len(height) - 1
        l_max = height[left]
        r_max = height[right]

        while (left <= right):
            if (l_max < r_max):
                if (l_max < height[left]):
                    l_max = height[left]
                else:
                    total += l_max - height[left]
                left += 1
            else:
                if (r_max < height[right]):
                    r_max = height[right]
                else:
                    total += r_max - height[right]
                right -= 1
        return total(root.left, L, R) + 0 + self.rangeSumBST(root.right, L, R)