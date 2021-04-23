#include <string>
#include <vector>
#include <iostream>
#include "prob.h"
//#include "test.h"
#include "prob.h"


bool unitTest(){
  std::vector<int> testData = {9, 11, 8, 5, 7, 10};
  int result = myFunction(testData);
  bool output = (5 == result);
  if(result)
  {
    std::cout << "pass!";
  }
  else
  {
    std::cout << "fail!";
  }
  return output;
}
int main()
{
  printProb();
  unitTest();
  return 0;
}
