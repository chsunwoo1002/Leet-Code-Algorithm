# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Time Complexity: O(logN), Space Complexity O(N) - List of Ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = self.foundLevel(root, 0)
        ans = [[] for i in range(level + 1)]
        self.orderTraversal(root, 0, ans)
        return ans

    def foundLevel(self, root, level):
        if root is None:
            return level - 1
        else:
            return max(self.foundLevel(root.left, level + 1), self.foundLevel(root.right, level + 1))

    def orderTraversal(self, root, level, ans):
        if root is None:
            return
        else:
            self.orderTraversal(root.left, level + 1, ans)
            ans[level].append(root.val)
            self.orderTraversal(root.right, level + 1, ans)
