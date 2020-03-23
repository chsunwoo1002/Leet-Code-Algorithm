# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tmp = ListNode(0)
        while (l1 != None or l2 != None):
            if (l1 != None and l2 != None):
                if (l1.val < l2.val):
                    tmp.next = l1
                    l1 = l1.next
                else:
                    tmp.next = l2
                    l2 = l2.next
            elif (l1 == None and l2 != None):
                tmp.next = l2
                l2 = l2.next
            elif (l1 != None and l2 == None):
                tmp.next = l1
                l1 = l1.next
            else:
                break
            tmp = tmp.next
        return head.next

