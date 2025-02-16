/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy=new ListNode(-1);
        
        ListNode* prev=dummy;
        ListNode* p1=list1;
        ListNode* p2=list2;
        while(p1!=NULL && p2!=NULL){
            if(p1->val < p2->val){
                prev->next=p1;
                prev=p1;
                p1=p1->next;
            
            }
            else{
                prev->next=p2;
                prev=p2;
                p2=p2->next;
            }
        }
        if(p1!=NULL){
            prev->next=p1;
        }
        if(p2!=NULL){
            prev->next=p2;
        }
        return dummy->next;

    }
};