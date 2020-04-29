# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findDiameter(root)
        return self.ans

    def findDiameter(self, root):
        if root is None:
            return 0

        left = self.findDiameter(root.left)
        right = self.findDiameter(root.right)
        if self.ans < left + right:
            self.ans = left + right

        return max(left, right) + 1