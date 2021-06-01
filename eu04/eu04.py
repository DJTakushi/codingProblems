def maxPalindrome(digits):
    #find all produts , put the in descending order, and check if they*re a palindrome
    #there must be a better way to do this.
    import math
    maxNum=int(math.pow(10,digits)-1)
    productSet=set()

    for i in range(1,maxNum+1):
        for j in range(1,maxNum+1):
            productSet.add(i*j)
    productList=list(productSet)
    productList.sort(reverse=True)
    for i in productList:
        if isPalindrome(i):
            return i
    return -1

def isPalindrome(input):
    arr=getDigitArray(input)
    lidx, hidx = 0, len(arr)-1
    while(lidx <= hidx):
        if(arr[lidx]!=arr[hidx]):
            return False
        lidx+=1
        hidx-=1
    return True
def getDigitArray(input):
    output=list()
    while input > 0:
        output.append(input%10)
        input//=10
    return output
