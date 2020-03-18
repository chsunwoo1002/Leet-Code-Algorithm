# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        count = 0
        dic = {}
        for index, i in enumerate(strs):
            key = tuple(sorted(i))
            if key in dic:
                ans[dic[key]].append(i)
            else:
                dic[key] = count
                ans.append([])
                ans[count].append(i)
                count += 1
        return ans
