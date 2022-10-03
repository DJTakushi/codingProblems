#include <iostream>
#include <assert.h>
#include <addTwoNumbers.h>
using namespace std;
int test(void)
{
  int o = -1;
  cout <<"function testing addTwo..."<<endl;
  Solution sol;

  cout << "testing getDescription()..." <<endl;
  vector<string> d = sol.getDescription();
  // for(auto i = d.begin(); i !=d.end();i++) cout << *i <<endl;
  assert(3==d.size());
  assert(d[0].npos != d[0].find("addTwo"));
  assert(d[1].npos != d[1].find("adds Two numbers provided as linked lists"));
  assert(d[2].npos != d[2].find("https://leetcode.com/problems/add-two-numbers/"));


  {
    string s1 = "2 4 3";
    string s2 = "5 6 4";
    string e = "7 0 8";
    cout << "testing ["<<s1<<"]+["<<s2<<"]==>["<<e<<"]...";
    ListNode* n1 = createNodeList(s1);
    ListNode* n2 = createNodeList(s2);
    Solution s = Solution();
    ListNode* a = s.addTwoNumbers(n1,n2);
    string r = getNodeListString(a);
    assert(e==r);
    cout<<"pass"<<endl;
  }
  {
    string s1 = "0";
    string s2 = "0";
    string e = "0";
    cout << "testing ["<<s1<<"]+["<<s2<<"]==>["<<e<<"]...";
    ListNode* n1 = createNodeList(s1);
    ListNode* n2 = createNodeList(s2);
    Solution s = Solution();
    ListNode* a = s.addTwoNumbers(n1,n2);
    string r = getNodeListString(a);
    assert(e==r);
    cout<<"pass"<<endl;
  }
  {
    string s1 = "9 9 9 9 9 9 9";
    string s2 = "9 9 9 9";
    string e = "8 9 9 9 0 0 0 1";
    cout << "testing ["<<s1<<"]+["<<s2<<"]==>["<<e<<"]...";
    ListNode* n1 = createNodeList(s1);
    ListNode* n2 = createNodeList(s2);
    Solution s = Solution();
    ListNode* a = s.addTwoNumbers(n1,n2);
    string r = getNodeListString(a);
    assert(e==r);
    cout<<"pass"<<endl;
  }
  cout <<"tests complete."<<endl;
  o = 0;
  return o;
}

int main(int argc, char* argv[]){
  return test();
}
