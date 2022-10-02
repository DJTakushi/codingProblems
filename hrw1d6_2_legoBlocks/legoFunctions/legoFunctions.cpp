#include "legoFunctions.h"
#include <iostream>
#include <chrono>
#include <list>
#include <math.h>
void getVector(int l, int max, vector<vector<int>>* out){
		/** l = length of row
				max = max block length **/
		// vector<vector<int>> out;
		if(l>=0)
		{
				if(l==0){
						vector<int> tmp;
						out->push_back(tmp);
				}else if(l==1){
						vector<int> tmp;
						tmp.push_back(1);
						out->push_back(tmp);
					} else if(l > 1)
					{
						for(int i = 1; i <= max; i++){
							int newl = l-i;
							if(newl>=0)
							{
								vector<vector<int>> recursive;
								getVector(newl,max, &recursive);
								for(auto it = recursive.begin();it!=recursive.end();it++)
								{
									it->insert(it->begin(),i);
									out->push_back(*it);
								}
							}
						}
					}
				}

}
set<int> getCrackIdx(vector<int> i){
	/** return set of indexes in a row where cracks occur for the block arrangement**/
	set<int> out;
	int sum = 0;
	for(auto it=i.begin();it!=i.end()-1;it++)
	{
		sum+=*it;
		out.insert(sum);
	}
	return out;
}
void setAnd(set<int>* a, set<int>* b, set<int>* out){
	/*** returns the AND of two sets ***/
	for(auto it = a->begin(); it!=a->end(); it++)
	{
		if(b->find(*it)!=b->end()) out->insert(*it);
	}
}
int countBadWalls(int n, list<set<int>>* options, set<int>* crackIdxs)
{	//recursive count the number of bad iterations
	int output = 0;
	if(n==0){
		if(crackIdxs->size()>0)output = 1;//cracks exist - count this as bad
		else output = 0;//cracks do not exist - bad
	}
	else
	{
		if(crackIdxs->size()>0)
		{
			for(auto it= options->begin(); it != options->end(); it++)
			{
				set<int>crackIdxs_t;
				// crackIdxs_t = crackIdxs;
				setAnd(crackIdxs, &(*it), &crackIdxs_t);//continue any shared cracks, forgive any that are mended
				output+=countBadWalls(n-1,options,&crackIdxs_t);//increment by recursive call
			}
		}
	}
	return output;
}
int legoBlocks(int n, int m){
	/** n = height of wall
	m = width of wall
	returns number of possible combinations **/
	auto start = chrono::steady_clock::now();
	auto startT = start;
	int out = 0;

	vector<vector<int>> uro;  //unrestricted row options
 	getVector(m,4, &uro);
	auto getVectorTimeDiff = chrono::steady_clock::now()-startT;

	startT = chrono::steady_clock::now();
	list<set<int>> uroList;
	for(auto it = uro.begin();it!=uro.end();it++){
		set<int> s = getCrackIdx(*it);
		uroList.push_back(s);
	}
	auto get_uroSetTime = chrono::steady_clock::now()-startT;

	cout << "uroList.size="<<uroList.size()<<endl;
	//printVectorVector(uro);
	startT = chrono::steady_clock::now();
	set<int>crackIdxsBlank;
	for(int i = 0; i < m; i++)
		crackIdxsBlank.insert(i);
	if(n >0){
			out = pow(uroList.size(), n)- countBadWalls(n,&uroList,&crackIdxsBlank);
	}
	auto buildWallsTime = chrono::steady_clock::now()-startT;
	auto totalDiff = chrono::steady_clock::now()-start;
	chrono::duration<double> totalDiff_s = chrono::duration_cast<chrono::duration<double>>(totalDiff);
	long td_0 = getVectorTimeDiff.count();
	long td_1 = get_uroSetTime.count();
	long td_2 = buildWallsTime.count();
	long td_t = totalDiff.count();
	float tdp_0 = 100*float(td_0)/td_t;
	float tdp_1 = 100*float(td_1)/td_t;
	float tdp_2 = 100*float(td_2)/td_t;

	cout <<"    completed getVector("<<m<<","<<4<<") in time diff "<<td_0<<"("<<tdp_0<<"%)"<<endl;
	cout <<"    completed getting uroSet in time diff "<<td_1<<"("<<tdp_1<<"%)"<<endl;
	cout <<"    completed buildWalls in time diff "<<td_2<<"("<<tdp_2<<"%)"<<endl;
	cout <<"    completed in "<<totalDiff_s.count()<<" seconds"<<endl;
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
