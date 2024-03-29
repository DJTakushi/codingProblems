#include <string>
#include <assert.h>
#include <testHelper.h>
#include <legoBlocksInterfaceConfig.h>
#include <legoFunctions/legoFunctions.h>
using namespace std;
int testSharedLibrary(void){
  cout <<"testSharedLibrary()..."<<endl;

  int m = 1;
  int n = 1;
  int exp = 1;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  int o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  m=2;
  n=2;
  exp=3;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=2;
  m=3;
  exp=9;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=4;
  m=4;
  exp=3375;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=4;
  m=5;
  exp=35714;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=4;
  m=6;
  exp=447902;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=4;
  m=7;
  exp=5562914;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=5;
  m=4;
  exp=29791;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=6;
  m=4;
  exp=250047;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  n=7;
  m=4;
  exp=2048383;
  cout << "testing legoBlocks("<<n<<","<<m<<") == "<<exp<<"...";
  o = legoBlocks(n,m);
  assert(exp==o);
  cout <<"pass"<<endl;

  return 0;
}

int testInterface(void){
  //https://pubs.opengroup.org/onlinepubs/9699919799/functions/popen.html
  cout <<"testInterface()..."<<endl;


  string command ="./lb 1 \"2 3\"";
  string exp = "9";
  cout << "testing command: " <<command <<" returns "<<exp<<"...";
  vector<string> o = commandToStrings(command);
  assert(1 == o.size());
  assert(exp==trim(o[0]));
  cout <<"pass."<<endl;

  return 0;
}
int main(int argc, char* argv[]){
  if(argc >1){
    // cout << "argc = "<< argc<<endl;
    string s = argv[1];
    // cout << "argv[1] = "<< s <<endl;
    if(s=="i"){
      assert(0==testInterface());
    }
    else{
      cout << "invalid option.  Use 'i' for interface, and no option for library"<<endl;
    }
  }
  else{
    assert(0==testSharedLibrary());
  }
  cout << "successfuly exiting" <<endl;
  return 0;
}
