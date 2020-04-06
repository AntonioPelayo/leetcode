/* Antono Pelayo April 5, 2020
Problem: 19. Remove Nth Node From End of List
Difficulty: Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
*/

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* fast = head;
        ListNode* slow = head;

        // Get the fast pointer n nodes away from the slow pointer
        for (int i = 0; i < n; i++) {
            fast = fast->next;
            if (!fast) 
                return head->next;
        } 
        
        // Move both nodes until fast has reached end of list
        while (fast->next) {
            slow = slow->next;
            fast = fast->next;
        }
           
        slow->next = slow->next->next;    // Skip over node n
        
        return head;
    }
};