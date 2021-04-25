#include <string>
#include <vector>
#include <iostream>
#include "prob.h"
//#include "test.h"
#include "prob.h"

class testCase{
public:
    std::vector<int> data;
    int expectation;
    testCase(std::vector<int> d, int exp){
      data = d;
      expectation = exp;
    }
};
bool unitTest(){
  std::vector<testCase> testCases;
  testCases.push_back(testCase({9, 11, 8, 5, 7, 10},5));
  testCases.push_back(testCase({9, 11, 8, 5, 7, 10,11},6));
  testCases.push_back(testCase({9, 11, 8, 5, 7, 10,11,0,15},15));

  bool result = true;
  for (auto it = begin(testCases); it != end(testCases);++it)
  {
    int testResult = myFunction(it->data);
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
