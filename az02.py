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

import takTest as tt
def functionWrapper(data):
    return find_sum_of_two(data.arr,data.target)
class fdata(tt.tData):
    def __init__(self,arr,target):
        self.arr=arr
        self.target=target
class TestMe(tt.tunittest):
    def makeTestVector(self):
        self.functionWrapper=functionWrapper
        tv=list()
        tv.append(tt.testCase(fdata([5,7,1,2,8,4,3],10),True))
        tv.append(tt.testCase(fdata([5,7,1,2,8,4,3],19),False))
        return tv
if __name__ == "__main__":
    tt.unittest.main()
