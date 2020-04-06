# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pMap = {}
        cmpMap = {}
        anaLength = len(p)
        ans = []

        for i in range(anaLength):
            pMap[p[i]] = pMap.get(p[i], 0) + 1

        for i in range(len(s)):
            cmpMap[s[i]] = cmpMap.get(s[i], 0) + 1
            if cmp(cmpMap, pMap) == 0:
                ans.append(i - anaLength + 1)
            if i - anaLength + 1 >= 0:
                cmpMap[s[i - anaLength + 1]] -= 1
                if cmpMap[s[i - anaLength + 1]] == 0:
                    del cmpMap[s[i - anaLength + 1]]

        return ans
