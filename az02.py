from takTest import *
def printPrompt():
    print("2. Determine if the sum of two integers is equal to the given value\n"
            "Given an array of integers and a value, determine if there\n"
            "are any two integers in the array whose sum is equal to the\n"
            "given value. Return true if the sum exists and return false if\n"
            "it does not. Consider this array and the target sums:\n"
            "  [5,7,1,2,8,4,3] targetsum=10  --> Yes(7+3, 2+8)\n"
            "  [5,7,1,2,8,4,3] targetsum=19  --> No\n"
            "Complete in O(n)\n"
            "HINT!!!  A set can be checked for a value with complexity O(1)!!!")


def find_sum_of_two(A, val):
    hashSet=set()
    for i in A:
        compliment=val-i
        if compliment in hashSet:
            return True
        hashSet.add(i)
    return False

def myFunctionW(data):
    return find_sum_of_two(data.arr,data.target)
class fdata:
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
    def print(self):
        print("  arr = "+str(self.arr))
        print("  target = "+str(self.target))
def getTestVector():
    tv=[]
    tv.append(testCase(fdata([5,7,1,2,8,4,3],10),True))
    tv.append(testCase(fdata([5,7,1,2,8,4,3],19),False))
    return tv
test(myFunctionW, getTestVector())
