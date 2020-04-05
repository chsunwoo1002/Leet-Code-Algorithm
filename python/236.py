# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.findAncestor(root, p, q)

    def findAncestor(self, root, p, q):

        if root is None or root is p or root is q:
            return root

        left = self.findAncestor(root.left, p, q)
        right = self.findAncestor(root.right, p, q)

        if left is None:
            return right
        elif right is None:
            return left
        else:  # if both are None or if common ancestor is found
            return root
