#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def printPrompt():
    print("14. Find Low/High Index\n"
            "Given a sorted array of integers, return the low and high index\n"
            "of the given key. You must return -1 if the indexes are not\n"
            "found. The array length can be in the millions with many\n"
            "duplicates.\n"
            "Consider the Array:\n"
            "    IDX[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]\n"
            "    VAL 1   2   5   5   5   5   5   5   5   5   20\n"
            "In the above example, according to the key, the low and\n"
            "high indices would be:\n"
            "  key: 1, low = 0 and high = 0\n"
            "  key: 2, low = 1 and high = 1\n"
            "  key: 5, low = 2 and high = 9\n"
            "  key: 20, low = 10 and high = 10\n\n"
            "Runtime Complexity: Logarithmic, O(logn)\n"
            "Memory Complexity: Constant, O(1)")
def find_low_index(arr, key):
    poI=find_pointOfImpact(arr,key)
    if poI==-1:
        return poI
    while poI != 0:
        if arr[poI-1] == key:
            poI-=1
        else:
            return poI
    return poI

def find_high_index(arr, key):
    poI=find_pointOfImpact(arr,key)
    if poI==-1:
        return poI
    while poI != (len(arr)-1):
        if arr[poI+1] == key:
            poI+=1
        else:
            return poI
    return poI

def find_pointOfImpact(arr,key):
    arrSize=len(arr)
    if key < arr[0]:
        return -1
    if key > arr[arrSize-1]:
        return -1
    cIdx=arrSize-1
    divPow=2
    prevIdx=0
    while arr[cIdx] != key:
        #print("...cIdx="+str(cIdx))
        step=arrSize//divPow
        if step==0:
            step=1
        #print("..step="+str(step))
        if arr[cIdx] > key:
            cIdx-=step
        else:
            cIdx+=step
        if cIdx==prevIdx:
            break
        else:
            prevIdx=cIdx
        divPow*=2
    return cIdx

def test():
    class testCase:
        def __init__(self,arr=list(),key=0,low=0,high=0):
            self.arr=arr
            self.key=key
            self.low=low
            self.high=high

    tar0=[1,2,5,5,5,5,5,5,5,5,20]
    testVector=list()
    testVector.append(testCase(tar0,1,0,0))
    testVector.append(testCase(tar0,2,1,1))
    testVector.append(testCase(tar0,5,2,9))
    testVector.append(testCase(tar0,20,10,10))
    tar1=[1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,6,6]
    testVector.append(testCase(tar1,1,0,2))
    testVector.append(testCase(tar1,2,3,7))
    testVector.append(testCase(tar1,3,8,10))
    testVector.append(testCase(tar1,4,11,14))
    testVector.append(testCase(tar1,5,15,17))
    testVector.append(testCase(tar1,6,18,23))
    testVector.append(testCase(tar1,8,-1,-1))


    for test in testVector:
        resultLow=find_low_index(test.arr,test.key)
        resultHigh=find_high_index(test.arr,test.key)
        failFlag=False
        if test.low!=resultLow:
            print("FAIL!!! Array "+str(test.arr)+ " with key "+str(test.key)+" expects low idx "+str(test.low)+" but produced "+str(resultLow)+" !")
            failFlag=True
        if test.high!=resultHigh:
            print("FAIL!!! Array "+str(test.arr)+ " with key "+str(test.key)+" expects high idx "+str(test.high)+" but produced "+str(resultHigh)+" !")
            failFlag=True
        if not failFlag:
            print("Pass.")
test()
