#include <string>
#include <vector>
#include <iostream>
#include "prob.h"
#include "main.h"
#include "solution.h"
//#include "test.h"

class testCase{
public:
    testCase(node * n, int e)
    {
      headNode = n;
      expectation = e;
    }
    node * headNode;
    int expectation;
};

bool unitTest(){
  std::vector<testCase> testCases;

  node * head = new node("*");
  head->l = new node("+");
  head->l->l = new node("3");
  head->l->r = new node("2");
  head->r = new node("+");
  head->r->l = new node("4");
  head->r->r = new node("5");
  testCases.push_back(testCase(head,45));

  head = new node("*");
  head->l = new node("*");
  head->l->l = new node("3");
  head->l->r = new node("2");
  head->r = new node("*");
  head->r->l = new node("4");
  head->r->r = new node("5");
  testCases.push_back(testCase(head,120));

  head = new node("/");
  head->l = new node("-");
  head->l->l = new node("556");
  head->l->r = new node("223");
  head->r = new node("+");
  head->r->l = new node("762");
  head->r->r = new node("308");
  testCases.push_back(testCase(head,0));

  head = new node("*");
  head->l = new node("-");
  head->l->l = new node("556");
  head->l->r = new node("223");
  head->r = new node("+");
  head->r->l = new node("762");
  head->r->r = new node("308");
  testCases.push_back(testCase(head,356310));

  bool result = true;
  for (auto it = begin(testCases); it != end(testCases);++it)
  {
    int testResult = myFunction(it->headNode);
    if (testResult != it->expectation)
    {
      result = false;
      std::cout<<"Fail!  Expected "<<it->expectation<<", but received "<<testResult<<"\n";
    }
  }
  if(result)
    std::cout<<"Pass!"<<"\n";
  return result;
}
int main()
{
  printProb();
  unitTest();
  return 0;
}
