# 1290. Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        num = 0
        length = 0
        ptr = head
        while ptr is not None:
            length = length + 1
            ptr = ptr.next
        ptr = head
        while ptr is not None:
            if ptr.val is not 0:
                num = num + pow(2, length - 1)
            length = length - 1
            ptr = ptr.next
        return num
