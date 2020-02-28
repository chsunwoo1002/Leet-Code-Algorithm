# 623. Add One Row to Tree
# https://leetcode.com/problems/add-one-row-to-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if (d == 1):
            newNode = TreeNode(v)
            newNode.left = root
            return newNode
        self.insertNode(root, v, d, 1)
        return root

    def insertNode(self, root, v, d, level):
        if root is None:
            return
        else:
            if (d == level + 1):
                leftNew = TreeNode(v)
                leftNew.left = root.left
                rightNew = TreeNode(v)
                rightNew.right = root.right
                root.left = leftNew
                root.right = rightNew
            else:
                self.insertNode(root.left, v, d, level + 1)
                self.insertNode(root.right, v, d, level + 1)