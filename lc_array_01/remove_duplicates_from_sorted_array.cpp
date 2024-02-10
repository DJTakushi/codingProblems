#include "remove_duplicates_from_sorted_array.h"

int Solution::removeDuplicates(std::vector<int>& nums) {
  std::vector<int>::iterator it = nums.begin();
  while(it < nums.end()){
    std::vector<int>::iterator jt = it;
    while(jt < nums.end() && *jt == *it){
      jt++;
    }
    if(*it == *(jt-1)){
      nums.erase((it+1), jt);
    }
    it++;
  }
  return nums.size();
}