#include "addTwoNumbers.h"

ListNode* Solution::addTwoNumbers(ListNode* l1, ListNode* l2){
  ListNode* o = NULL;
  ListNode* cNode = o;
  int carry = 0;
  while((l1!=NULL) | (l2!=NULL) | (carry != 0)){
    int i1 = 0;
    int i2 = 0;
    if(l1!=NULL){
      i1=l1->val;
      l1=l1->next;
    }
    if(l2!=NULL){
      i2=l2->val;
      l2=l2->next;
    }
    int sum = i1+i2+carry;
    carry = sum/10;
    sum = sum%10;
    if(o==NULL){
        o = new ListNode(sum);
        cNode = o;
    }
    else{
      cNode->next = new ListNode(sum);
      cNode = cNode->next;
    }
  }
  return o;
}

