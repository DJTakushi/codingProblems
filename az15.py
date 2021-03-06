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

# key<Mid LSorted key>Lmin RSorted key<Rmax Dir
#    1       1      1         x       x      L
#    1       1      0         x       x      R
#    1       0      x         x       x      L
#    0       x      x         1       1      R
#    0       x      x         1       0      L
#    0       x      x         0       x      R


def binary_search_rotated(arr, key):
    s=0#start
    e=len(arr)-1
    m=((e-s)//2)+s
    while(arr[m] != key):
        #print("s,m,e = "+str(s)+","+str(m)+","+str(e))
        if s==e:
            return -1
        if key < arr[m]:
            if arr[s] < arr[m] and key < arr[s]:
                s=m+1
            else:
                e=m-1
        else:
            if arr[m] < arr[e] and key > arr[e]:
                e=m-1
            else:
                s=m+1
        m=((e-s)//2)+s
    return m


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

    additional=True
    if additional:
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
        # if counter>1:
            # return
        result=binary_search_rotated(test.arr,test.key)
        if test.expectation!=result:
            print("FAIL!!! Array "+str(test.arr)+ " with key "+str(test.key)+" expects "+str(test.expectation)+" but produced "+str(result)+" !")
        else:
            print("Pass.")
        counter+=1
test()
