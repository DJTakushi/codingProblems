
// PROBLEM STATEMENT:
//
// Given a list L of M arrays of ints, where each array is sorted
// in ascending order, collect the K smallest elements among
// all the arrays.
//
// Constraints:
// 1 <= M <= 10^5
// 0 <= K <= 10^5
// L[i].size() is unbounded, for i in [0, M)
//
// Example:
// K = 7
// M = 3
// L[0] = {10, 20, 30, 40, 50, 60, 70, 80}
// L[1] = {15, 25, 35, 45, 55, 65, 75}
// L[2] = {-2, 3, 11, 15, 53, 55, 90}
// Ans  = {-2, 3, 10, 11, 15, 15, 20}

#include <cstdint>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>

// Memory complexity: O(?)
// Time complexity: O(?)
std::vector<int> collect_top_k(const std::vector<std::vector<int>>& lists, std::size_t k)
{
  std::vector<int> o;//output
  std::vector<int> ci;//current indexes
  std::set<std::pair<int, int>> set;
  std::multimap<int, int> x;
  std::priority_queue<std::tuple<int, int, int>> q;

  std::map<int, int> lowestValues;//key = lowest value, value = pair (lowest value in list
  for(size_t i = 0; i < lists.size();i++) lowest//ci.push_back(0);
  for(size_t i = 0; i<k;i++){
    // std::vector<int> temporaryMins;
    int minCandidate = INT32_MAX;
    int minCandidateIdx = -1;
    for(int j = 0; j<lists.size();j++){//iterating through each list
      int t_idx=ci[j];//temporay index
      size_t listMaxIdx =lists[j].size()-1;
      if(t_idx<=listMaxIdx){
        if(lists[j][t_idx]<minCandidate){
            minCandidate = lists[j][t_idx];
            minCandidateIdx = j;
        }
      }
    }
    if(minCandidateIdx<0) break;
    o.push_back(minCandidate);
    ci[minCandidateIdx]++;

  }

  return o;
}

int main() {
  const std::vector<std::vector<int>> lists = {
      {10, 20, 30, 40, 50, 60, 70, 80},
      {15, 25, 35, 45, 55, 65, 75},
      {-2, 3, 11, 15, 53, 55, 90},
  };

  std::size_t num_elems = 0;
  for (const auto &list : lists)
    num_elems += list.size();

  for (std::size_t k = 0; k < num_elems + 3; ++k) {
    const auto ans = collect_top_k(lists, k);

    std::cout << k << ':';
    for (const auto &elem : ans)
      std::cout << ' ' << elem;
    std::cout << '\n';
  }

  std::cout << "Part 1 done." << std::endl;

  {
    std::vector<std::vector<int>> many_lists(
        100'000, std::vector<int>({1, 2, 3, 4, 5, 6, 7, 8}));

    const auto big_ans = collect_top_k(many_lists, 100'000);

    std::cout << "big_ans:";
    for (std::size_t i = 0; i < 20; ++i)
      std::cout << ' ' << big_ans[i];
    std::cout << " ...\n";
  }

  std::cout << "Part 2 done." << std::endl;
}
