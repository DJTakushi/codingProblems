#https://www.educative.io/blog/crack-amazon-coding-interview-questions
from takTest import *
def printPrompt():
    print("Determine if the sum of two integers is equal to the given value\n"
            "Given an array of integers and a value, determine if there\n"
            "are any two integers in the array whose sum is equal to the\n"
            "given value. Return true if the sum exists and return false\n"
            "if it does not. Consider this array and the target sums:\n"
            "  5  7  1  2  8  4  3\n"
            "  Target Sum=10, 7+3=10, 2+8=10:  True\n"
            " Target Sum=19, No 2 values sum up to 19\n"
            "Runtime Complexity: Linear, O(n)\n"
            "Memory Complexity: Linear, O(n)")

def functionW(data):
    return print_all_braces(data.input)
def print_all_braces(n):
  result=set()
  myList=list()
  myList.append('{')
  result=bracesRecursive(n,myList,result)
  return result
def bracesRecursive(n,theList,theSet):
    #print(theList)
    #print(type(theList))
    curLen=len(theList)
    if curLen>(n*2):
        return theSet
    lCount=0
    rCount=0
    for iter in theList:
        if iter=='{':
            lCount+=1
        if iter=='}':
            rCount+=1
    if curLen==(n*2):
        if lCount==rCount:
            theListTuple=tuple(theList)
            if theListTuple not in theSet:
                theSet.add(theListTuple)
                # print("ADDED! "+ str(theListTuple))
    else:
        theList.append('{')
        theSet=bracesRecursive(n,theList.copy(),theSet)
        theList.pop(-1)
        if rCount < lCount:
            theList.append('}')
            theSet=bracesRecursive(n,theList.copy(),theSet)
    return theSet
class fdata:
    def __init__(self,input):
        self.input=input
    def print(self):
        print("  input = "+str(self.input))
def getTestVector():
    tv=[]
    tv.append(testCase(fdata(1),{('{','}')}))
    tv.append(testCase(fdata(2),{('{','{','}','}'),('{','}','{','}')}))
    tv.append(testCase(fdata(3),{('{', '{', '{', '}', '}', '}'),('{', '{', '}', '{', '}', '}'),('{', '{', '}', '}', '{', '}'),('{', '}', '{', '{', '}', '}'),('{', '}', '{', '}', '{', '}')}))
    return tv
test(functionW, getTestVector())
