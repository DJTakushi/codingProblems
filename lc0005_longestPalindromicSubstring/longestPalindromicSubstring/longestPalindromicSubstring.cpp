#include <longestPalindromicSubstring.h>
#include <map>
bool Solution::isPalindrome(string s){
    cout << "isPalindrome("<<s<<")...";
    bool o = true;
    int s_l = s.size();//string length
    int midpoint = s_l/2;
    for(int i = 0; i < midpoint; i++)
    {
        char l = s[i];
        char r = s[s_l-1-i];
        if(l!=r){
            // cout <<s[i]<<"!="<<s[s_l-1-i]<<endl;
            o = false;
            break;
        }
    }
    cout <<o<<endl;
    return o;
}
string Solution::longestPalindrome(string s) {
    string o = s.substr(0,1);
    int o_l = o.size();//o length
    int s_l = s.size();//s length
#ifdef BRUTE_FORCE
    //brute-force - check each possible substring and record max (O(n*n*n))
    for(int i = 0; i < s_l;i++){//i = start idx
        for(int j = 0; j <= s_l-i; j++){//j = length of substr
            string subS = s.substr(i,j);
            int subS_l =subS.size();
            if(isPalindrome(subS) && subS_l>o_l){
                o = subS;
                o_l = subS_l;
            }
        }
    }
#else
#ifdef FIRM_FORCE
    map<char, vector<int>> charIdxM;//char-index map (vector represents indexes where character occurs)

    for(int i = 0; i < s_l; i++){//populate charIdxM
        char ct = s[i];//char_temp
        map<char, vector<int>>::iterator it = charIdxM.find(ct);
        if(it!=charIdxM.end()) it->second.push_back(i); // add to back of vector
        else charIdxM[ct]={i}; // create fresh vector for this char
    }
    for(auto it = charIdxM.begin(); it!=charIdxM.end();it++){//iterate through map's keys (characters)
        vector<int> idxV = it->second;

        bool maxAchieved=false;//max possible palindome found for this char
        for(auto start = idxV.begin(); start <idxV.end();start++){
            for(auto endI = idxV.rbegin(); endI<idxV.rend();endI++){
                if(*start != *endI){
                    int len_t = *endI-*start+1;//temporarey length of this substring
                    string subS = s.substr(*start, len_t);
                    int subS_l =subS.size();
                    if(isPalindrome(subS) && subS_l>o_l){
                        o = subS;
                        o_l = subS_l;
                        break;
                    }
                }
            }
            if(maxAchieved)break;
        }
    }
#else
//iterate along characters in string
  for(size_t i = 0; i < s.size(); i++){
    string ot; //o temp

    // set left and right indexes to this char
    size_t left = i;
    size_t right = i;

    // while left==right (it's a palindrome)
    while(true){
      //  if can increase left and right indexes, do it

      size_t leftNew = left-1;
      size_t rightNew = right+1;
      if((left>0 & right < s_l-1)
            && (s[leftNew]==s[rightNew])){
        left--;
        right++;
      }
      //  if not, break
      else break;
    }
    ot=s.substr(left,right-left+1);
    cout << "i:"<<to_string(i)<<", ot="<<ot<<endl;
    // record substring if a record
    o = ot.size() > o.size() ? ot : o;
  }

// improvemnt! start in middle of s, and then iterate right/left.  Stop iterating if potential palindrome length is lower than record length

#endif
#endif
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
