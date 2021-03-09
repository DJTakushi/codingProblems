def printProblem():
    print("Find the missing number in the array\n"
            "  You are given an array of positive numbers from 1 to n,\n"
            "  such that all numbers from 1 to n are present except one\n"
            "  number x. You have to find x. The input array is not sorted.\n"
            "  Look at the below array and give it a try before checking\n"
            "  the solution.\n"
            "  3 7 1 2 8 4 5\n"
            "  n = 8\n"
            "Runtime Complexity: Linear, O(n)\n"
            "Memory Complexity: Constant, O(1)O(1)")

def find_missing(input):
    sum=0
    lowestNum=input[0]
    highestNum=input[0]
    for i in input:
        sum+=i
        if i<lowestNum:
            lowestNum=i
        if i>highestNum:
            highestNum=i
    expectedSum=0
    for i in range(lowestNum,highestNum+1):
        expectedSum+=i
    difference=expectedSum-sum

    if difference!=0:
        return difference
    return -1

import takTest as tt
def functionWrapper(data):
    return(find_missing(data.arr))
class fdata(tt.tData):
    def __init__(self,arr):
        self.arr=arr
class TestMe(tt.tunittest):
    def makeTestVector(self):
        self.functionWrapper=functionWrapper
        testVector=list()
        testVector.append(tt.testCase(fdata([3,7,1,2,8,4,5]),6))
        testVector.append(tt.testCase(fdata([3,7,1,2,8,4,5,10,9]),6))
        testVector.append(tt.testCase(fdata([3,7,1,2,8,4,5,10,9,12,6]),11))
        return testVector
if __name__ == "__main__":
    tt.unittest.main()
