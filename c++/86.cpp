//86. Partition List
//https://leetcode.com/problems/partition-list/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        if(head == NULL){
            return head;
        }
        ListNode* point = head;
        if(point -> val < x){
            while(point -> next != NULL && point -> next-> val < x){
                point = point -> next;
            }
        }
        ListNode* current = point -> next;
        ListNode* prev = point;
        while(current != NULL){
            if(current -> val < x){
                if(point->val >= x){
                    prev -> next = current -> next;
                    current -> next = point;
                    point = current;
                    current = prev;
                    head = point;
                }
                else {
                    prev -> next = current -> next;
                    current -> next = point -> next;
                    point -> next = current;
                    point = point -> next;
                }
            }
            prev = current;
            current = current -> next;
        }
        return head;
    }
};
