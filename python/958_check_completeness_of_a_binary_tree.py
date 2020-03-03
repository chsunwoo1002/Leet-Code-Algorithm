# 958. Check Completeness of a Binary Tree
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        count = self.numOfNode(root) # get total number of nodes
        return self.checkCompleteTree(root, 1, count)

    def checkCompleteTree(self, root, current, numNode):
        # when root is null,
        # the number of nodes is less than current node position number if we assume it is complete tree
        if root is None:
            if current <= numNode:
                return False
            else:
                return True
        else:
            # when root is not null,
            # the number of nodes is larger than current node position number if we assume it is complete tree
            if current > numNode:
                return False
            else:
                return self.checkCompleteTree(root.left, current * 2, numNode) and self.checkCompleteTree(root.right,
                                                                                                          current * 2 + 1,
                                                                                                          numNode)

    def numOfNode(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.numOfNode(root.left) + self.numOfNode(root.right)