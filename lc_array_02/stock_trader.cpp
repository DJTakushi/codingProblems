#include "stock_trader.h"

int Solution::maxProfit(std::vector<int>& prices){
  int profit = 0;
  std::vector<int>::iterator it = prices.begin();
  while(it != (prices.end()-1)){
    if(*it < *(it+1)){
      profit += *(it+1)-*it;
    }
    it++;
  }
  return profit;
};