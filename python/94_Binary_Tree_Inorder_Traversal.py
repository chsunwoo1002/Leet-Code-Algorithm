# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        ans = []
        stack = []
        current = root
        stack.append(root)

        while stack != []:
            while current is not None and stack != []:
                stack.append(current)
                current = current.left
            tmp = stack.pop()
            ans.append(tmp.val)
            current = tmp.right

        ans.pop(len(ans) - 1) # root is pushed twice, so last one should be deleted

        return ans