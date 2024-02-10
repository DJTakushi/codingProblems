#include "stock_trader.h"

int Solution::maxProfit(std::vector<int>& prices){
  int profit = 0;
  int last = prices[0];
  std::vector<int>::iterator it = prices.begin()+1;
  int val;
  while(it != prices.end()){
    val = *it;
    if(val > last){
      profit += val-last;
    }
    last = val;
    it++;
  }
  return profit;
};