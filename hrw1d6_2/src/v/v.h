#include <vector>
#include <set>
#include <string>
using namespace std;
vector<vector<int>> getVector(int l, int max, vector<int> vIn);

set<int> getCrackIdx(vector<int> i);
bool vectorsCrack(vector<int> a, vector<int>b);

vector<vector<int>> getComplimentOptions(vector<int> base, vector<vector<int>> options);

void printVectorVector(vector<vector<int>> v);
void printVector(vector<int> v);
string getVectorString(vector<int>v);
int solve(int n, int m);
int solve2(int n, int m);

int buildWalls(int n, vector<vector<int>>* options, set<int> crackIdxs);
set<int> setAnd(set<int> a,set<int>b);
void printSet(set<int> ms, string prefix);
