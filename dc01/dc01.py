def canSumToKey(arr, key):
    sArr = list(arr)
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
