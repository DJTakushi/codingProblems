#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def printPrompt():
    print("15. Search Rotated Array\n"
            "Search for a given number in a sorted array, with unique\n"
            "elements, that has been rotated by some arbitrary number.\n"
            "Return [-1] if the number does not exist.\n"
            "Assume that the array does not contain duplicates.\n"
            "For example, below is an origianl array before rotation:\n"
            "[0]   [1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]   [9]   [10]  [11]  [12]  [13]  [14]  [15]  [16]  [17]  [18]  [19]\n"
            "[1]   [10]  [20]  [47]  [59]  [63]  [75]  [88]  [99]  [107] [120] [133] [155] [162] [176] [188] [199] [200] [210] [222]\n"
            "After performign rotatin on this array 6 times, it chagnes to:\n"
            "[0]   [1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]   [9]   [10]  [11]  [12]  [13]  [14]  [15]  [16]  [17]  [18]  [19]\n"
            "[176] [188] [199] [200] [210] [222] [1]   [10]  [20]  [47]  [59]  [63]  [75]  [88]  [99]  [107] [120] [133] [155] [162]\n"
            "Runtime Complexity: Logarithmic,O(logn)\n"
            "Memory Complexity: Logarithmic,O(logn)\n")
def binary_search_rotated(arr, key):
    arrLen=len(arr)
    cIdx=arrLen//2
    count=2
    while(arr[cIdx] != key):
        step=arrLen//(2*count)
        print("cIdx="+str(cIdx)+" step="+str(step))
        if step==0:
            step=1
        leftSorted=False
        rightSorted=False
        if arr[cIdx-step]<arr[cIdx]:
            leftSorted=True
        if arr[cIdx]<arr[cIdx+step]:
            rightSorted=True
        if leftSorted:
            leftMin=arr[cIdx-(2*step)]
            if key < arr[cIdx] and key >= leftMin:
                cIdx-=step
        else:
            rightMax=arr[cIdx+(2*step)]
            if key > arr[cIdx] and key <= rightMax:
                cIdx+=step
            else:
                cIdx-=step
                print("HOW DID I GET HERE?!?")
    return cIdx


def test():
    class testCase:
        def __init__(self,arr=list(),key=0,exp=0):
            self.arr=arr
            self.key=key
            self.expectation=exp

    tar0=[1,10,20,47,59,63,75,88,99,107,120,133,155,162,176,188,199,200,210,222]
    testVector=list()
    counter=0
    for iter in tar0:
        testVector.append(testCase(tar0,iter,counter))
        counter+=1
    tar1=[176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
    counter=0
    for iter in tar1:
        testVector.append(testCase(tar1,iter,counter))
        counter+=1
    tar2=[47,59,63,75,88,99,107,120,133,155,162,176,188,199,200,210,222,1,10,20]
    counter=0
    for iter in tar2:
        testVector.append(testCase(tar2,iter,counter))
        counter+=1

    counter=0
    for test in testVector:
        if counter>1:
            break
        result=binary_search_rotated(test.arr,test.key)
        if test.expectation!=result:
            print("FAIL!!! Array "+str(test.arr)+ " with key "+str(test.key)+" expects "+str(test.expectation)+" but produced "+str(result)+" !")
        else:
            print("Pass.")
test()
