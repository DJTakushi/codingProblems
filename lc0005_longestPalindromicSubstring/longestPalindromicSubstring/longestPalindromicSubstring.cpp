#include <longestPalindromicSubstring.h>
#include <map>

string Solution::getPalindromeAtRoot(string s, int i, size_t left, size_t right){
  string o(1,s[i]); //output
  size_t s_l = s.size();//s length

  // while left==right (it's still a palindrome)
  while(s[left]==s[right]){
    //  if can increase left and right indexes, do it
    size_t leftNew = left-1;
    size_t rightNew = right+1;
    if((left>0 & right < s_l-1) //validate new indexes are in range
          && (s[leftNew]==s[rightNew])){//validate new indexes are palindromic
      left--;
      right++;
    }
    //  if should not advance, update o with last palindrome string and break to return
    else{
      o=s.substr(left,right-left+1);
      break;
    }
  }
  return o;
}

string Solution::longestPalindrome(string s) {
  string o = s.substr(0,1);

  //iterate along characters in string
  for(size_t i = 0; i < s.size(); i++){
    string ot; //o temp
    ot = this->getPalindromeAtRoot(s, i, i, i);//i is center of odd palindrome
    o = ot.size() > o.size() ? ot : o;

    //can try even palindrome with symmetry between i and i+1
    if(i<s.size()-1){
      ot = this->getPalindromeAtRoot(s, i, i, i+1);//in case even palindrome
      o = ot.size() > o.size() ? ot : o;
    }
  }

  /* TODO: try starting in middle of s, and then iterate right/left.
  Stop iterating if potential palindrome length is lower than record length.
  Middle will contain the longest palindrom (E.G: `AAAAAAAAAAAAAAAAAAAAAA`)*/
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
