// #include <cmath>
#include <iostream>
// #include <string>
#include "include/tutorialConfig.h"
#ifdef USE_MYMATH
	#include "MathFunctions.h"
#endif
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

int main(int argc, char *argv[]) {
	printProjectInfo();
	const double inputValue = std::stod(argv[1]);
	#ifdef USE_MYMATH
		const double outputValue = mysqrt(inputValue);
		cout <<"mysqrt("<<inputValue<<")="<<outputValue<<endl;
	#else
		const double outputValue = mysqrt(inputValue);
	#endif

	for(int i = 1; i < argc;i++)
	{
		cout << argv[i] << endl;
	}

	return 0;
}
