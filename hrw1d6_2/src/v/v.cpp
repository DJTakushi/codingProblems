#include "v.h"
#include <iostream>
vector<vector<int>> getVector(int l, int max, vector<int> vIn){
		/** l = length of row
				max = max block length
				vIn = previous row **/
		string vInS;
		cout <<"getVector("<<l<<","<<max<<")"<<endl;
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

		cout <<"getVector("<<l<<","<<max<<") returns "<<out.size()<<" options"<<endl;
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
bool vectorsCrack(vector<int> a, vector<int>b){
	set<int> aC = getCrackIdx(a);
	set<int> bC = getCrackIdx(b);
	// cout << "vectorsCrack("<<getVectorString(a)<<","<<getVectorString(b)<<"):"<<endl;
	// printSet(aC, "aC:");
	// printSet(bC, "bC:");
	for(auto it = aC.begin(); it!=aC.end();it++)
	{
		if(bC.find(*it)!=bC.end())
		{
			// cout <<*it<<" found in aC and bC.  Returning false"<<endl;
			return false;
		}
	}

	// cout <<" no cracks found.  Returning true"<<endl;
	return true;
}

vector<vector<int>> getComplimentOptions(vector<int> base, vector<vector<int>> options){
	// vector<vector<int>> out;
	// if(base.size()==0) out = options;
	// else{
		vector<vector<vector<int>>::iterator> toErase;
		for(auto it= options.begin(); it!=options.end();it++)
			if(!vectorsCrack(base, *it))
			{
				cout<<"  erasing "<<getVectorString(*it)<<endl;
				toErase.push_back(it);
			}

		for(auto it=toErase.rbegin(); it != toErase.rend();it++)//iterate backwards to keep earlier indexing intact
			options.erase(*it);
	// }
		string baseString = getVectorString(base);
		cout<<"getComplimentOptions("<<getVectorString(base)<<",uro):"<<endl;
		printVectorVector(options);
	return options;
}
int solve(int n, int m){
	/** n = height of wall
	m = width of wall
	returns number of possible combinations **/
	int out = 0;
	vector<int> dummy;
	vector<vector<int>> uro = getVector(m,4, dummy);  //unrestricted row options
	if(n>=1){
		out = uro.size();
		vector<vector<int>> baseRow = uro;
		cout <<"BaseRow("<<1<<"): "<<endl;
		printVectorVector(baseRow);
		for(int i = 1; i < n; i++)
		{
			vector<vector<int>> compliments;
			for(auto vit = baseRow.begin(); vit != baseRow.end();vit++)
			{
				vector<vector<int>> compliments_t = getComplimentOptions(*vit, uro);
				compliments.insert(compliments.end(), compliments_t.begin(), compliments_t.end());
			}
			baseRow.clear();
			baseRow.insert(baseRow.end(), compliments.begin(),compliments.end());

			cout <<"BaseRow(new)("<<i<<"): "<<endl;
			printVectorVector(baseRow);
			out=baseRow.size(); //duplicates included since they take different paths

			//remove duplicates by putting into a set and then back into a vector
			// set<vector<int>> setTemp;
			// for(auto it = baseRow.begin();it!=baseRow.end();it++)setTemp.insert(*it);
			// baseRow.clear();
			//
			// for(auto it = setTemp.begin();it!=setTemp.end();it++)baseRow.push_back(*it);
		}
	}

	return out;
}


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
