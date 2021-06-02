def findMissingPositiveInteger(a):
    loopCount = 0
    for tIdx in range(len(a)):
        while a[tIdx] != tIdx and a[tIdx] != 0:
            loopCount+=1
            if a[tIdx] < 0:
                a[tIdx]=0 #zero negatives
            target = a[tIdx]
            if target <= len(a)-1:
                if a[target] == target: #it's dulicate, so let's remove this
                    a[tIdx]= 0
                else:
                    tempThisVal = a[tIdx]
                    a[tIdx]=a[target]
                    a[target]=tempThisVal
            else:
                if target == len(a): #may be more appropraiate to use a +1
                    a.append(target)
                else:
                    a[tIdx]=0#out of range; just zero this guy
            # print(a)
    print("loops/len = "+str(loopCount/len(a))+"("+str(loopCount)+"/"+str(len(a))+")")
    for tIdx in range(len(a)):
        if tIdx != a[tIdx]:
            return tIdx
    return a[len(a)-1]+1
