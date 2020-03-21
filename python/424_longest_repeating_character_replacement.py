# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_counts = {}
        most_frequency = 0
        maxLen = 0
        start = 0
        for end in range(len(s)):
            char_counts[s[end]] = char_counts.get(s[end], 0) + 1
            most_frequency = max(most_frequency, char_counts[s[end]])
            if(end - start - most_frequency +1 > k):
                char_counts[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end-start + 1)
        return maxLen