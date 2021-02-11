description="#1. Find the missing number in the array\n"
description=description+"  You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.\n"
description=description+"  3 7 1 2 8 4 5\n"
description=description+"  n = 8 missing number = 6\n"
print(description)

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
 #TODO: Write - Your - Code
    return -1

testVector=[3,7,1,2,8,4,5]
testVector2=[3,7,1,2,8,4,5,10,9]
print(str(find_missing(testVector)))
print(str(find_missing(testVector2)))
