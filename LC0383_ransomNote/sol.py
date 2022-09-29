# https://leetcode.com/problems/ransom-note/
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        o = True
        d = self.getDict(magazine)
        for i in ransomNote:
            try:
                d[i]-=1
                if d[i]<0:
                    o = False
            except:
                o = False
        return o
    def getDict(self, magazine):
        o = {}
        for i in magazine:
            try:
                o[i]+=1
            except:
                o[i]=1
        return o

if __name__=="__main__":

    sol = Solution()
    mag = "b"
    rNote = "a"
    assert False == sol.canConstruct(rNote,mag)

    rNote = "aa"
    mag = "ab"
    assert False == sol.canConstruct(rNote,mag)

    rNote = "aa"
    mag="aab"
    assert True == sol.canConstruct(rNote,mag)

    rNote = "aa"
    mag="aab"
    assert True == sol.canConstruct(rNote,mag)
