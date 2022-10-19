#include <solution.h>

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
void invalidReturn(void){
  cout <<"invalid arguments"<<endl;
}

int main(int argc, char* argv[])
{
    switch(argc){
      case 0:
      case 1:
        printProjectInfo();
        break;
      case 2:
        {
          string s = argv[1];
          if(s=="d")
          {
            cout << "Library Details:"<<endl;
            Solution s = Solution();
            vector<string> v = s.getDescription();
            for(auto i = v.begin(); i!=v.end();i++)
            {
              cout << "  "<<*i<<endl;
            }
          }
          else if(s=="t")
          {
            cout << "TODO: running function tests..."<<endl;
            // todo - run function test from library if linking to extra libraries is deemed worthwhile
          }
          else
          {
            invalidReturn();
          }
        }
        break;
      case 3:
        {
          //Solution s = Solution();
          cout << "TODO - handle calls to solution HERE!!!" << endl;
        }
        break;
      default:
        invalidReturn();
        break;
    }

  return 0;
}
