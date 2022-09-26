#include "v.h"
#include <iostream>
vector<vector<int>> getVector(int l, int max, vector<int> vIn){
		/** l = length of row
				max = max block length
				vIn = previous row **/
		string vInS;
		vector<vector<int>> out;
		if(l>=0)
		{
				if(l==0){
						vector<int> tmp;
						out.push_back(tmp);
				}else if(l==1){
						vector<int> tmp;
						tmp.push_back(1);
						out.push_back(tmp);
					} else if(l > 1)
					{
						for(int i = 1; i <= max; i++){
							int newl = l-i;
							if(newl>=0)
							{
								vector<vector<int>> recursive = getVector(newl,max,vIn);
								for(auto it = recursive.begin();it!=recursive.end();it++)
								{
									it->insert(it->begin(),i);
									out.push_back(*it);
								}
							}
						}
					}
				}
    return out;
}
set<int> getCrackIdx(vector<int> i){
	set<int> out;
	int sum = 0;
	for(auto it=i.begin();it!=i.end()-1;it++)
	{
		sum+=*it;
		out.insert(sum);
	}
	return out;
}
set<int> setAnd(set<int> a,set<int>b){
	set<int> out;
	for(auto it = a.begin(); it!=a.end(); it++)
	{
		if(b.find(*it)!=b.end()) out.insert(*it);
	}
	return out;
}
int buildWalls(int n, vector<vector<int>>* options, set<int> crackIdxs)
{/** n - remaining height
	options = pointer to options for row (uro)
	crackIdxs indeces where there is a crack.  may be empty!**/
	int output = 0;
	if(n==0){
		if(crackIdxs.size()==0)output = 1;//no cracks exist - good
		else output = 0;//cracks exist - bad
	}
	else
	{
		for(auto it= options->begin(); it != options->end(); it++){//can actually just look at options as a vector of set<ints>
			set<int>crackIdxs_t = setAnd(crackIdxs, getCrackIdx(*it));//continue any shared cracks, forgive any that are mended
			output+=buildWalls(n-1,options,crackIdxs_t);//increment by recursive call
		}
	}
	return output;
}
int legoBlocks(int n, int m){
	/** n = height of wall
	m = width of wall
	returns number of possible combinations **/
	int out = 0;
	vector<int> dummy;
	vector<vector<int>> uro = getVector(m,4, dummy);  //unrestricted row options
	// cout << "uro:"<<endl;
	//printVectorVector(uro);
	set<int>crackIdxsBlank;
	for(int i = 0; i < m; i++)
		crackIdxsBlank.insert(i);
	if(n >0){
			out = buildWalls(n,&uro,crackIdxsBlank);
	}
	return out;
}
#ifdef PRINT_FUNCTIONS
void printVectorVector(vector<vector<int>> v)
{
	for(auto it = v.begin(); it!=v.end();it++)
	{
		for(auto j = it->begin();j!=it->end();j++)
		{
			cout<<*j<<" ";
		}
		cout<<endl;
	}
}
void printVector(vector<int> v)
{
	for(auto it = v.begin(); it!=v.end();it++) cout<<*it<<" ";
	cout<<endl;
}
string getVectorString(vector<int>v)
{
	string out;
	for(auto i = v.begin();i!=v.end();i++) out+=to_string(*i)+" ";
	return out;
}
void printSet(set<int> ms, string prefix){
	cout << prefix;
	for(auto i = ms.begin();i!=ms.end();i++)cout << *i << " ";
	cout << endl;
	return;
}
#endif
