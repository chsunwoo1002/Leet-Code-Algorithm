# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class Solution(object):
    def evenNumbers(self, num):
        count = 0
        while num != 0:
            num = num / 10
            count = count + 1
        if count % 2 is 0:
            return True
        else:
            return False

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            if self.evenNumbers(i) is True:
                count = count + 1
        return count
