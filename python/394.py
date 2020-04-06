#394. Decode String
# https://leetcode.com/problems/decode-string/
# Time Complexity O(N), Space Complexity O(N)
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        ans, num = "", ""
        stack = []
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append((int(num), ans))
                num, ans = "", ""
            elif char == ']':
                digit, tmp = stack.pop()
                ans = tmp + digit * ans
            else:
                ans += char
        return ans
