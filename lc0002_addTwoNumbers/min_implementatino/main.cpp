// g++ -g -Wall -O2 main.cpp addTwoNumbers.cpp -o main
#include <assert.h>
#include "addTwoNumbers.h"

int main(int argc, char *argv[])
{
  ListNode *n1 = new ListNode(2, new ListNode(4, new ListNode(3)));
  ListNode *n2 = new ListNode(5, new ListNode(6, new ListNode(4)));

  Solution s = Solution();
  ListNode *a = s.addTwoNumbers(n1, n2);
  assert(a->val == 7);
  assert(a->next->val == 0);
  assert(a->next->next->val == 8);

  cout << "pass" << endl;

  return 0;
}
