#include <string>
#include <vector>
#include <iostream>
#include "prob.h"
#include "main.h"
#include "solution.h"
//#include "test.h"

class testCase{
public:
    testCase(std::string s)
    {
      url = s;
    }
    std::string url;
};
extern "C" {
  BUTT bool unitTest(){
    std::vector<testCase> testCases;

    testCases.push_back(testCase("y33t"));
    testCases.push_back(testCase("beetz"));
    testCases.push_back(testCase("y33t"));
    testCases.push_back(testCase("0"));
    testCases.push_back(testCase("1"));
    testCases.push_back(testCase("4"));
    testCases.push_back(testCase("556"));
    testCases.push_back(testCase("762"));
    testCases.push_back(testCase("762"));
    testCases.push_back(testCase("762 SOVIET"));

    bool result = true;
    urlManager* myUrlManager = new urlManager();
    for (auto it = begin(testCases); it != end(testCases);++it)
    {
      std::string out = myUrlManager->shorten(it->url);
      out = myUrlManager->restore(out);
      if (out != it->url)
      {
        result = false;
        std::cout<<"Fail!  Expected \""<<it->url<<"\", but received \""<<out<<"\"\n";
      }
    }
    if(result)
      std::cout<<"Pass!"<<"\n";
    return result;
  }
}
int main()
{
  //printProb();
  unitTest();
  return 0;
}
