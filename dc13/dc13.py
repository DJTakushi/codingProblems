def printProblem():
    print(" Problem #13 [Hard]\n"
            "This problem was asked by Amazon.\n"
            "Given an integer k and a string s, find the length of the\n"
            "longest substring that contains at most k distinct characters.\n"
            "For example, given s = \"abcba\" and k = 2, the longest substring\n"
            " with k distinct characters is \"bcb\".")

def maxStrWithKUnique(inStr,k):
    countUniqueChars.c=0

    alphaDict=dict()#key = letter, value=list of indexs where char is in string
    for i in range(len(inStr)):
        thisLetter=inStr[i]
        if thisLetter in alphaDict:
            alphaDict[thisLetter].append(i)
        else:
            alphaDict[thisLetter]=[i]
    print(alphaDict)
    #find duplicates that can be used
    #see if each dulicate can be used

    return -1

def DUMBmaxStrWithKUnique(inStr,k):#O(n^3)
    record=""
    while inStr:
        for i in range(len(inStr)+1):
            tempStr = inStr[0:i]
            if countUniqueChars(tempStr)<=k:
                if len(tempStr)>len(record):
                    record=tempStr
        inStr=inStr[1:]
    print(str(countUniqueChars.c))
    return record



def countUniqueChars(inStr):
    charSet=set()
    for i in range(len(inStr)):
        charSet.add(inStr[i])
        countUniqueChars.c+=1
    return len(charSet)
countUniqueChars.c=0

import unittest
class myTests(unittest.TestCase):
    def testThis(self):
        self.assertEqual(4,countUniqueChars("Danny"))
        self.assertEqual(6,countUniqueChars("Daniel"))
        self.assertEqual(4,countUniqueChars("Mississippi"))
        self.assertEqual(3,countUniqueChars("abcba"))

        self.assertEqual("bcb",maxStrWithKUnique("abcba",2))
        self.assertEqual("",maxStrWithKUnique("abcba",0))
        self.assertEqual("a",maxStrWithKUnique("abcba",1))
        self.assertEqual("abcba",maxStrWithKUnique("abcba",3))
        self.assertEqual("ississippi",maxStrWithKUnique("Mississippi",3))

if __name__=="__main__":
    unittest.main()
