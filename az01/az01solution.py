def my_find_missing(input):
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
