# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.checkSameTree(p,q)

    def checkSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            if(p.val != q.val):
                return False
            else:
                return self.checkSameTree(p.left, q.left) and self.checkSameTree(p.right, q.right)
        else:
            return False