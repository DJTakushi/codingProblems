from takTest import *
#Given a list of numbers and a number k, return whether any two numbers
#from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

def myFunctionW(data):#wrapper to unwrap data and then call function
    return(myFunction(data.arr,data.key))
def myFunction(arr, key):
    sArr = arr.copy()
    sArr.sort()
    for i in range(len(sArr)):
        if sArr[i]>key: #first item is too large to be possible; all after fail
            return False
        for j in range(i,len(sArr)):
            if sArr[j] > key:#all after are too big
                continue
            sum=sArr[i]+sArr[j]
            if sum==key:
                return True
            if sum > key:
                continue
    return False
class fdata:
    def __init__(self,arr,key):
        self.arr=arr
        self.key=key
    def print(self):
        print("  arr = "+str(self.arr))
        print("  key = "+str(self.key))

testVector=list()
testVector.append(testCase(fdata([10,15,3,7],17),True))
testVector.append(testCase(fdata([10,15,3,8],17),False))
testVector.append(testCase(fdata([15,3,8],17),False))
testVector.append(testCase(fdata([15,2,8],17),True))
testVector.append(testCase(fdata([15,2],17),True))
testVector.append(testCase(fdata([15,1,2,3,4,5,6,7,8],17),True))
testVector.append(testCase(fdata([0,2,4,6,8,10,12,14,16,18,20],17),False))
test(myFunctionW, testVector)
