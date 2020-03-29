# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        today = len(T) - 1
        ans = [0] * (today + 1)
        maxTemp = 100
        dayMap = {}

        while today >= 0:
            future = float('inf')
            temp = T[today] + 1
            while temp <= maxTemp:
                if temp in dayMap:
                    future = min(future, dayMap[temp])
                temp += 1
            dayMap[T[today]] = today
            if future == float('inf'):
                ans[today] = 0
            else:
                ans[today] = future - today
            today -= 1

        return ans