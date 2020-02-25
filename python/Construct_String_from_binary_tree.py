# 606. Construct String from Binary Tree
# https://leetcode.com/problems/construct-string-from-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.stringBT(t)
    def stringBT(self, t):
        if t is None:
            return ""
        else:
            left = right = ""
            if(t.left != None):
                left = "(" + self.stringBT(t.left) + ")"
            if(t.right != None):
                right = "(" + self.stringBT(t.right) + ")"
            if(right != "" and left == ""):
                return str(t.val) + "()" + right
            return str(t.val) + left + right