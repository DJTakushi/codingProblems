#include <solution.h>
#include <map>
#include <set>
#include <algorithm>

void printWordInstances(map<string,int> inMap){
  return;
  for(auto it = inMap.begin();it!=inMap.end();it++)
  {
    cout <<"inMap[" << it->first << "]:"<<to_string(it->second)<<endl;
  }
}
void printocv(vector<set<string>> ocv){
  return;
  for(size_t i = 0; i<ocv.size();i++){
    cout<<"ocv["<<to_string(i)<<"]:";
    for(auto jt = ocv[i].begin();jt!=ocv[i].end();jt++){
      cout<<*jt;
      if(std::next(jt,1) != (ocv[i].end())) cout <<", ";
    }
    cout<<endl;
  }
}


// TODO - define functions here!!!
vector<string> Solution::topKFrequent(vector<string>& words, int k) {
  vector<string> o;

  //create dictionary (key=word, value=occurrences) (o(n))
  std::map<string,int> wordInstances; //(key=word, value=occurrences)
  std::vector<std::set<string>> ocv;//occurrence vector (index=numberOfOccurences), value = set of words that exist withThisQuantity
  ocv.push_back({});//push back empty set at idx0
  ocv.push_back({});//push back empty set at idx1

  for(auto it = words.begin();it!=words.end();it++){
    auto wi_i = wordInstances.find(*it);//wordInsatnce interator
    if(wi_i==wordInstances.end()){// new word
      wordInstances[*it]=1;// set count to 1
      ocv[1].insert(*it);// add to set at idx1
    }
    else{
      //remove from ocv at old index
      ocv[wordInstances[*it]].erase(*it);

      //increment wordInstances count
      wordInstances[*it]++;

      //ensure ocv has enough indexes for new index
      while((ocv.size()-1)<wordInstances[*it])
        ocv.push_back({}); //push back empty set

      //add to ocv at new index
      ocv[wordInstances[*it]].insert(*it);
    }
  }

  printWordInstances(wordInstances);
  printocv(ocv);
  
  // get elements at rear of vector
  while(o.size() < k){
    //remove back of ocv if this index is empty
    while(ocv.back().size()<=0) ocv.pop_back();

    string t;
    auto myLast = (ocv.back().begin());
    t = *myLast;
    o.push_back(t);

    // pop from back
    ocv.back().erase(t);
  }
  printocv(ocv);

  return o;
}

vector<string> Solution::getDescription(){
  vector<string> o;
  string title = string(PROJECT_NAME);
  title+=" "+to_string(VERSION_MAJOR)
        +"."+to_string(VERSION_MINOR);
  string desc = "  ";
  desc += PROJECT_DESCRIPTION;
  string url = "  ";
  url+=PROJECT_HOMEPAGE_URL;
    o.push_back(title);
    o.push_back(desc);
    o.push_back(url);
  return o;
}
