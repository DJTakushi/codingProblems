#include <iostream>
#include <string>
#include <legoBlocksInterfaceConfig.h>
#include <legoFunctions/legoFunctions.h>

using namespace std;
void printProjectInfo(){
	string pName = PROJECT_NAME;
	string maj = to_string(VERSION_MAJOR);
	string min = to_string(VERSION_MINOR);
	string desc = PROJECT_DESCRIPTION;
	string url = PROJECT_HOMEPAGE_URL;
	cout << pName<< " "<<maj<<"."<< min<<endl;
	cout << "  description: "<<desc<<endl;
	cout << "  homepage url: "<<url<<endl;
	return;
}

int main(int argc, char* argv[])
{
  int t = 0;
  int n = 0, m = 0;
  int spaceIdx = 0;
  string s;
  switch(argc){
    case 0:
    case 1:
      printProjectInfo();
      break;
    default:
      t = std::stoi(argv[1]);
      for(int i = 0; i < t;i++)
      {
        s = argv[2+i];
        spaceIdx = s.find(" ");
        // cout <<"spaceIdx="<<spaceIdx<<endl;
        string a = s.substr(0,spaceIdx);
        // cout << "a="<<a;
        n = stoi(a);
        string b =s.substr(spaceIdx+1, string::npos);
        // cout <<" b="<<b<<endl;
        m = stoi(b);
        // cout << "n="<<n<<", m="<<m << endl;
        // vector<int> vIn;
        // vector<vector<int>> v = getVector(m,4,vIn);
        // printVector(v);
				// cout << "solve("<<n<<","<<m<<"):"<<endl;
				int out = legoBlocks(n,m);
				cout <<out<<endl;
      }
      // getVector(0,vIn);
      break;
  }
  return 0;
}
