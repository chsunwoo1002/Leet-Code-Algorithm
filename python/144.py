# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        stack = []
        stack.append(root)
        ans = []

        while stack != []:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            if tmpNode.right is not None:
                stack.append(tmpNode.right)
            if tmpNode.left is not None:
                stack.append(tmpNode.left)

        return ans