#include <string>
#include <vector>
#include <iostream>
#include "prob.h"
//#include "test.h"

class testCase{
public:
    node headNode;
    int expectation;
};

bool unitTest(){
  std::vector<testCase> testCases;
  node * head = new node("*");
  head.l = new node("+");
  head.l.l = new node("3");
  head.l.r = new node("2");
  head.r = new node("+");
  head.r.l = new node("4");
  head.r.r = new node("5");

  testCases.push_back(testCase(head,45));

  bool result = true;
  for (auto it = begin(testCases); it != end(testCases);++it)
  {
    std::string testResult = myFunction(it->headNode);
    if (testResult != it->expectation)
    {
      result = false;
      std::cout<<"Fail!"<<"\n";
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
