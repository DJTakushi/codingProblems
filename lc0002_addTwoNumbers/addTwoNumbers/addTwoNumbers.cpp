#include <addTwoNumbers.h>

ListNode* Solution::addTwoNumbers(ListNode* l1, ListNode* l2){
  ListNode* o = NULL;
  ListNode* cNode = o;
  int carry = 0;
  while(l1!=NULL | l2!=NULL | carry != 0){
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

vector<string> Solution::getDescription(){
  vector<string> o;
  string title = string(PROJECT_NAME);
  title+=" "+to_string(VERSION_MAJOR)
        +"."+to_string(VERSION_MINOR);
  string desc = "  ";
  desc += PROJECT_DESCRIPTION;
  string url = "  ";
  url+=PROJECT_HOMEPAGE_URL;
    o.push_back(title);
    o.push_back(desc);
    o.push_back(url);
  return o;
}
ListNode* createNodeList(string i){
  ListNode* head = NULL;
  ListNode* cNode = head;

  while(i.size() > 0)
  {
    int delim = i.find(" ");
    string front = i.substr(0,delim);
    int val = stoi(front);

    if(head==NULL){
      head = new ListNode(val);
      cNode = head;
    }
    else{
      cNode->next = new ListNode(val);
      cNode = cNode->next;
    }
    if(delim != i.npos) i = i.substr(delim+1, i.npos);
    else i = "";
  }
  return head;
}
string getNodeListString(ListNode* head){
  string o;
  while(head != NULL)
  {
      o+=to_string(head->val);
      if(head->next != NULL) o+=" ";
      head = head->next;
  }
  return o;
}
