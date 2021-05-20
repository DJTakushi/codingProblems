#include <string>
#include <vector>
#include <iostream>
#include <sstream>
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
  char * unitTest(){
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
    int counter = 0;
    std::stringstream buffer;
    for (auto it = begin(testCases); it != end(testCases);++it)
    {
      std::string out = myUrlManager->shorten(it->url);
      out = myUrlManager->restore(out);
      if (out != it->url)
      {
        result = false;
        buffer<<"Fail at case "<<counter<<"!  Expected \""<<it->url<<"\", but received \""<<out<<"\"\n";
      }
      counter++;
    }
    if(result)
      buffer<<"Pass!";

    std::string str = buffer.str();
    char *cstr = new char[str.length() + 1];//todo - clean up this memory leak
    strcpy(cstr, str.c_str());
    printf("returning address: %p\n", cstr);
    return cstr;
  }
}
void freeme(char *ptr)
{
    printf("freeing address: %p\n", ptr);
    free(ptr);
}
int main()
{
  //printProb();
  std::cout << unitTest();
  return 0;
}
