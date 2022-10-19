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
  cout << "sol != NULL..."<<endl;

  {
    vector<string> input = {"i", "love", "leetcode", "i","love","coding"};
    int k = 2;
    vector<string> output = sol->topKFrequent(input,k);

    // cout << "output: ";
    // for(auto it = output.begin();it!=output.end();it++) cout << *it <<" ";
    // cout <<endl;

    assert(2==output.size());
    assert("i"==output[0]);  
    assert("love"==output[1]);  
  }
  {
    vector<string> input = {"the","day","is","sunny","the","the","the","sunny","is","is"};
    int k = 4;
    vector<string> output = sol->topKFrequent(input,k);
    assert(4==output.size());
    assert("the"==output[0]);  
    assert("is"==output[1]);  
    assert("sunny"==output[2]);  
    assert("day"==output[3]);  
  }
  {
    vector<string> input = {"vbimix","ztj","ztj","vbimix","zgoedv","itnsxvvevu","bftirwsc","nlv","ithxcskb","walxnr","amkjox","ehzbw","ithxcskb","bftirwsc","amkjox","vbimix","ztj","amkjox","itnsxvvevu","ithxcskb","oveunzoevl","bdqinoduvu","tfbpcjj","itnsxvvevu","vbimix","tfbpcjj","rllqmb","iwj","iwj","ithxcskb","ehzbw","ehzbw","bdqinoduvu","vbimix","ithxcskb","ithxcskb","ehzbw","iwj","bdqinoduvu","nlv","tfbpcjj","nlv","ehzbw","ztj","ztj","tfbpcjj","oveunzoevl","itnsxvvevu","amkjox","vbimix","itnsxvvevu","ehzbw","iwj","rllqmb","itnsxvvevu","ehzbw","iwj","tfbpcjj","amkjox","vbimix","itnsxvvevu","amkjox","nlv","tfbpcjj","nlv","ztj","iwj","bftirwsc","bdqinoduvu","zgoedv","ithxcskb","itnsxvvevu","vbimix","walxnr","amkjox","bftirwsc","vbimix","itnsxvvevu","tfbpcjj","bdqinoduvu","ithxcskb","ithxcskb","ztj","bftirwsc","iwj","bftirwsc","tfbpcjj","ehzbw","ehzbw","amkjox","ztj","itnsxvvevu","zgoedv","nlv"};
    int k = 14;
    vector<string> output = sol->topKFrequent(input,k);
    assert(14==output.size());     
    assert("itnsxvvevu"==output[0]);  
    assert("ehzbw"==output[1]);  
    assert("ithxcskb"==output[2]);  
    assert("vbimix"==output[3]);  
    assert("amkjox"==output[4]);  
    assert("tfbpcjj"==output[5]);  
    assert("ztj"==output[6]);  
    assert("iwj"==output[7]);  
    assert("bftirwsc"==output[8]);  
    assert("nlv"==output[9]);  
    assert("bdqinoduvu"==output[10]);  
    assert("zgoedv"==output[11]);  
    assert("oveunzoevl"==output[12]);  
    assert("rllqmb"==output[13]);  
    // cout << "output: ";
    // for(auto it = output.begin();it!=output.end();it++) cout << *it <<" ";
    // cout <<endl;
  }



  delete sol;
  cout <<"tests complete."<<endl;
  return o;
}
int main(int argc, char* argv[]){
  return test();
}
