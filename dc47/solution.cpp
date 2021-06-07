#include   "solution.h"
int myFunction(std::vector<int> prices){
  int recordLow = 0;
  int recordHigh = 0;
  int currentLow = 0;

  for(int i = 0; i < prices.size(); i++){
    if(prices[i]<prices[currentLow])
    {
      currentLow = i;
    }
    int recordDiff = prices[recordHigh]-prices[recordLow];
    int currentDiff = prices[i]-prices[currentLow];

    if(currentDiff > recordDiff)
    {
      recordLow = currentLow;
      recordHigh = i;
    }
  }
  return prices[recordHigh]-prices[recordLow];
}

/** Wrapping true function with an array-inpu wrapper is easlier
    to interface with python's ctypes**/
int myFunctionArray(int* arrHead, int size)
{
  std::vector<int> tempVector;
  for(int i = 0; i < size; i++)
  {
      tempVector.push_back(arrHead[i]);
  }
  return myFunction(tempVector);
}
