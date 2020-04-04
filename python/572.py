# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.findSubtree(s, t)

    def findSubtree(self, s, t):
        if s is None:
            return False
        else:
            if s.val == t.val:
                return self.checkTrees(s, t) or self.findSubtree(s.right, t) or self.findSubtree(s.left, t)
            else:
                return self.findSubtree(s.right, t) or self.findSubtree(s.left, t)

    def checkTrees(self, s, t):
        if s is None and t is None:
            return True
        elif s is not None and t is not None:
            if s.val != t.val:
                return False
            else:
                return self.checkTrees(s.left, t.left) and self.checkTrees(s.right, t.right)
        else:
            return False