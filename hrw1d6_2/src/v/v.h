#include <vector>
#include <set>
#include <string>
using namespace std;
vector<vector<int>> getVector(int l, int max, vector<int> vIn);
set<int> getCrackIdx(vector<int> i);
set<int> setAnd(set<int> a,set<int>b);
int buildWalls(int n, vector<vector<int>>* options, set<int> crackIdxs);
int solve2(int n, int m);

#ifdef PRINT_FUNCTIONS
  void printVectorVector(vector<vector<int>> v);
  void printVector(vector<int> v);
  string getVectorString(vector<int>v);
  void printSet(set<int> ms, string prefix);
#endif
