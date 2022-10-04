// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Given a string s, find the length of the longest substring without repeating characters.
//
//
//
// Example 1:
//
// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:
//
// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:
//
// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//
//
// Constraints:
//
// 0 <= s.length <= 5 * 104
// s consists of English letters, digits, symbols and spaces.

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int>lastIdx; //last instance where char occurred
        int startIdx_c=-1; //start index of currently eligible word
        int maxLen=0;//max length

        // populate map
        for(int i = 0; i != s.size();i++)
        {
            char c = s[i];
            //get last occurrence of this char (-1 if hasn't occurred yet)
            int lastOccurrence = lastIdx.find(c)!=lastIdx.end()?lastIdx[c]:-1;

            //get the start index of this substring
            startIdx_c = startIdx_c>lastOccurrence?startIdx_c:lastOccurrence;

            int size_c = i - startIdx_c;
            if(size_c>maxLen)maxLen = size_c;

            lastIdx[c]=i;
        }
        if(startIdx_c==-1)maxLen = s.size();
        return maxLen;

    }
};
