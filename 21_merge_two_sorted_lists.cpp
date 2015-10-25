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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *p1 = l1;
        ListNode *p2 = l2;
        static ListNode dummy(0);
        ListNode *curNode = &dummy;
        
        while (p1 && p2){
            if (p1->val < p2->val) {
                curNode->next = p1;
                p1 = p1->next;
            }
            else{
                curNode->next = p2;
                p2 = p2->next;
            }
            curNode = curNode->next;
        }
        
        if (p1) curNode->next = p1;
        else curNode->next = p2;
        
        return dummy.next;
        
    }
};
