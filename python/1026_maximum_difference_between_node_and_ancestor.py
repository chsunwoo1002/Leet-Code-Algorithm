# 1026. Maximum Difference Between Node and Ancestor
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findDiff(root, root.val, root.val)

    def findDiff(self, root, maxNode, minNode):
        if root is None:
            return 0
        else:
            maxNode = max(maxNode, root.val)
            minNode = min(minNode, root.val)
            return max(maxNode - minNode,
                       max(self.findDiff(root.right, maxNode, minNode), self.findDiff(root.left, maxNode, minNode)))