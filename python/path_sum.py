# 112. Path Sum
# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.checkSumExist(root, sum)

    def checkSumExist(self, root, sum):
        if root is None: # cases that parents node has only one child
            return False
        else:
            if (root.left == None and root.right == None): # check leaf node 
                if sum - root.val is 0:
                    return True
                else:
                    return False
            else:
                return self.checkSumExist(root.left, sum - root.val) or self.checkSumExist(root.right, sum - root.val)