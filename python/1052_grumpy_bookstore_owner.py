# 1052. Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/submissions/
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        max_techique = 0
        not_grumpy = 0
        start = 0
        tmp = 0

        for end in range(len(customers)):
            if (end - start + 1 > X):
                if (grumpy[start] == 1): # when start pointer points out grumpy element, we remove that element
                    tmp -= customers[start]
                start += 1
            if (grumpy[end] == 0):
                not_grumpy += customers[end]
            else:
                tmp += customers[end]
            max_techique = max(max_techique, tmp) #compare maximum value with techique with current value

        return max_techique + not_grumpy