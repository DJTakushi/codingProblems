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

    while
    return -2

def find_high_index(arr, key):
    return -2

def find_pointOfImpact(arr,key):
    arrSize=len(arr)
    if key < arr[0]:
        return -1
    if key > arr[arrSize-1]:
        return -1
    cIdx=arrSize-1
    divPow=2
    while arr[cIdx] != key:
        step=arrSize/divPow
        if arr[cIdx] > key:
            cIdx-=step
        else:
            cIdx+=step
        divPow*=2
    return cIdx

def test():
    tar0=[1,2,5,5,5,5,5,5,5,5,20]
    tar1=[1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,6,6]
test()
