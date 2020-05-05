# 198. House Robber
# https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 0:
            return 0
        if len(nums) is 1:
            return nums[0]
        if len(nums) is 2:
            return max(nums[0], nums[1])

        ans = [0] * len(nums)
        ans[0] = nums[0]
        ans[1] = nums[1]

        for i in range(2, len(nums)):
            ans[i] = max(ans[:i - 1]) + nums[i]
        return max(ans)