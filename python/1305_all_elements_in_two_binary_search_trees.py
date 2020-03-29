# 1305. All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        first_list = []
        second_list = []
        self.treeIntoList(root1, first_list)
        self.treeIntoList(root2, second_list)
        first_list += second_list
        first_list.sort()
        return first_list

    def treeIntoList(self, root, treeList):
        if root is None:
            return
        else:
            self.treeIntoList(root.left, treeList)
            treeList.append(root.val)
            self.treeIntoList(root.right, treeList)