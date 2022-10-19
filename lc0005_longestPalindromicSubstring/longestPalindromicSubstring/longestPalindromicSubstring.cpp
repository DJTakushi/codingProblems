#include <longestPalindromicSubstring.h>
#include <map>

string Solution::longestPalindrome(string s) {
    string o = s.substr(0,1);
    int o_l = o.size();//o length
    int s_l = s.size();//s length

//iterate along characters in string
  for(size_t i = 0; i < s.size(); i++){
    string ot; //o temp

    // set left and right indexes to this char
    size_t left = i;
    size_t right = i;

    // while left==right (it's a palindrome)
    while(s[left]==s[right]){//not necessary to check here if left==right
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

    //TODO: rfactor this to make DRY code.
    // Consider function prototype:
    // string getPalindromeAtRoot(string s, int leftStart, int rightStart);
    if(i<s.size()-1){
      // set left and right indexes to this char
      left = i;
      right = i+1;

      // while left==right (it's a palindrome)
      while(s[left]==s[right]){
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
      if(s[left]==s[right]){//must check in case they were never equal
        ot=s.substr(left,right-left+1);
        cout << "i(2):"<<to_string(i)<<", ot="<<ot<<endl;
        // record substring if a record
        o = ot.size() > o.size() ? ot : o;
      }
    }

  }

// improvemnt! start in middle of s, and then iterate right/left.  Stop iterating if potential palindrome length is lower than record length
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
