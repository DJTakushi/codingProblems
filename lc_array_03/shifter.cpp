#include "shifter.h"
#include <string>
#include <iostream>
void printVector(std::vector<int> nums){
    std::string dbug = "[";
    for(auto i : nums){
      dbug += std::to_string(i) + ",";
    }
    dbug = dbug.substr(0,dbug.size()-1);
    dbug += "]";
    std::cout <<dbug<<std::endl;
}

void rotate1(std::vector<int>& nums, int k){
  k = k % nums.size();
  while(k > 0){
    std::vector<int> new_nums;

    new_nums.push_back(nums.back());
    for(size_t i = 0; i < (nums.size()-1); i++){
      new_nums.push_back(nums[i]);
    }

    for(size_t i = 0; i < nums.size(); i++){
      nums[i] = new_nums[i];
    }
    // printVector(nums);
    k--;
  }
}

void rotate2(std::vector<int>& nums, int k){
  int idx0 = nums[0];
  for(size_t i = 0; i < nums.size(); i++){
    size_t i_tgt = (nums.size()-1-k-i)%nums.size();
    nums[i]=nums[i_tgt];
  }
  nums
}

void Solution::rotate(std::vector<int>& nums, int k){
  return rotate1(nums,k);
};