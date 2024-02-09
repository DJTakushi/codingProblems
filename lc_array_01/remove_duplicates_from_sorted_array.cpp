#include "remove_duplicates_from_sorted_array.h"

int Solution::removeDuplicates(std::vector<int>& nums) {
  int k = 0;
  int last = -101;//out of cases's range
  for(size_t idx = 0; idx < nums.size(); idx++){
    if(last == nums[idx]){
      nums.erase(nums.begin()+idx);
      idx--;//go back
    }
    else{
      k++;
    }
    last = nums[idx];
  }
  return k;
}