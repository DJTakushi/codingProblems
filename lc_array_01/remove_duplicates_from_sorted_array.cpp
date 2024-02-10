#include "remove_duplicates_from_sorted_array.h"

int Solution::removeDuplicates(std::vector<int>& nums) {
  std::vector<int>::iterator it = nums.begin();
  while(it < nums.end()){
    std::vector<int>::iterator jt = it;
    while((jt+1) < nums.end() && *(jt+1) == *it){
      jt++;
    }
    if(it != jt){
      //Removes the elements in the range [first, last).
      nums.erase(it, jt);
    }
    it++;
  }
  return nums.size();
}