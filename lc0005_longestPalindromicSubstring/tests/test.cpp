#include <iostream>
#include <assert.h>
#include <longestPalindromicSubstring.h>
using namespace std;
int test(void)
{
  int o = -1;
  cout <<"function testing longestPalindromicSubstring..."<<endl;
  Solution sol;
  string ot="";//output-temporary
  string it="";//input-temporary

  it = "aba";
  ot = sol.longestPalindrome(it);
  assert("aba"==ot);

  it = "babad";
  ot=sol.longestPalindrome(it);
  assert("aba"==ot | "bab"==ot);

  it ="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth";
  ot=sol.longestPalindrome(it);
  assert("ranynar"==ot);

  it = "cbbd"; // leetcode case 73/140
  ot=sol.longestPalindrome(it);
  assert("bb"==ot);

  cout <<"tests complete."<<endl;
  return o;
}
int main(int argc, char* argv[]){
  return test();
}
