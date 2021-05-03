#include <string>
#include <vector>
#include <iostream>
#include "prob.h"
#include "main.h"
#include "solution.h"
//#include "test.h"

class testCase{
public:
    testCase(std::strign s)
    {
      url = s;
    }
    std::string url;
};

bool unitTest(){
  std::vector<testCase> testCases;

  testCases.push_back(testCase("y33t"));

  bool result = true;
  for (auto it = begin(testCases); it != end(testCases);++it)
  {
    std::string out = shorten(it->url);
    out = restore(out);
    if (out != it->url)
    {
      result = false;
      std::cout<<"Fail!  Expected "<<it->url<<", but received "<<out<<"\n";
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
