/* Antonio Pelayo April 6, 2020
Problem: 206 Reverse Linked List
Difficulty: Easy

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you 
implement both?
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
    ListNode* reverseList(ListNode* head) {
        ListNode* current = NULL;

        while (head) {
            // Place holders
            ListNode* next = head->next;
            head->next = current;
            
            // Move pointers forward
            current = head;
            head = next;
        }
        return current;
    }
};