# 101. Symmetric tree
# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, left, right):
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            if (left.val != right.val):
                return False
            else:
                return self.checkSymmetric(left.right, right.left) and self.checkSymmetric(left.left, right.right)
        else:
            return False