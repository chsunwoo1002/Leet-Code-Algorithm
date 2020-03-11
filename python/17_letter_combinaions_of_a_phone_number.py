# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def getAllLetters(self, ans, tmpStr, digits, length, graph):
        if length >= len(digits):
            ans.append(tmpStr)
        else:
            if int(digits[length]) > 1 and int(digits[length]) < 10:
                for i in graph.get(int(digits[length])):
                    self.getAllLetters(ans, tmpStr + i, digits, length + 1, graph)
            else:
                self.getAllLetters(ans, tmpStr, digits, length + 1, graph)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if (digits == ""):
            return None
        num_graph = {}
        num_graph[2] = ['a', 'b', 'c']
        num_graph[3] = ['d', 'e', 'f']
        num_graph[4] = ['g', 'h', 'i']
        num_graph[5] = ['j', 'k', 'l']
        num_graph[6] = ['m', 'n', 'o']
        num_graph[7] = ['p', 'q', 'r', 's']
        num_graph[8] = ['t', 'u', 'v']
        num_graph[9] = ['w', 'x', 'y', 'z']

        self.ans = []
        self.getAllLetters(self.ans, '', digits, 0, num_graph)
        return self.ansm