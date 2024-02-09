#include "remove_duplicates_from_sorted_array.h"
#include <iostream>
#include <string>
#include <vector>
void print_results(std::vector<int> v, int k){
  std::string printout = "[";
  for(auto i : v){
    printout += (std::to_string(i) + ","); 
  }
  printout = printout.substr(0,printout.size()-1);
  printout += std::string("] k = " + std::to_string(k));
  std::cout <<printout <<std::endl;

};
int main(int argc, char * argv[]){
  Solution s;
  int result;

  std::vector<int> ex1 = {1,1,2};
  result = s.removeDuplicates(ex1);
  print_results(ex1,result);

  std::vector<int> ex2 = {0,0,1,1,1,2,2,3,3,4};
  result = s.removeDuplicates(ex2);
  print_results(ex2,result);


  std::cout <<"done"<<std::endl;
}