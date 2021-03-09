from azBinTree import  *
#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def can_segment_string(s, dictionary):
    strLen=len(s)
    hashSet=set()
    for idx in range(strLen):
        markToContinue=False
        a=s[0:idx]
        b=s[idx:strLen]
        if a not in dictionary:
            hashSet.add(a)
            markToContinue=True
        if b not in dictionary:
            hashSet.add(b)
            markToContinue=True
        if not markToContinue:
            return True
    return False

import takTest as tt
def functionWrapper(data):
    return can_segment_string(data.s,data.dictionary)
class fdata(tt.tData):
    def __init__(self,s,dictionary):
        self.s=s
        self.dictionary=dictionary
class TestMe(tt.tunittest):
    def makeTestVector(self):
        self.functionWrapper=functionWrapper
        tv=list()
        dict={"apple","apple","pear","pie"}
        tv.append(tt.testCase(fdata("applepie",dict),True))
        tv.append(tt.testCase(fdata("applepeer",dict),False))
        dict={"peach","apple","pear","pie"}
        tv.append(tt.testCase(fdata("applepie",dict),True))
        tv.append(tt.testCase(fdata("applepeer",dict),False))
        dict={"hell","now","on","hello"}
        tv.append(tt.testCase(fdata("hellonow",dict),True))
        return tv
if __name__ == "__main__":
    tt.unittest.main()
