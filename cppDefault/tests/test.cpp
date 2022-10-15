#include <iostream>
#include <assert.h>
#include <solution.h>
using namespace std;
int test(void)
{
  int o = -1;
  cout <<"function testing solution..."<<endl;
  Solution* sol = new Solution();
  assert(sol != NULL);
  cout << "sol != NULL...";

  delete sol;
  cout <<"tests complete."<<endl;
  return o;
}
int main(int argc, char* argv[]){
  return test();
}
