def sumOfFactors(limit, factors):
    commonMultiple=1
    for i in factors: #could reduce this to use the LCM, but I can't now
        commonMultiple*=i
    addendSet=set()
    for i in factors:
        c=i
        while(c <= commonMultiple):
            addendSet.add(c)
            c+=i
    addendList=list(addendSet)
    addendList.sort() #may be probelmatic for very long lists
    base, sum = 0, 0
    while(base < limit):
        for i in addendList:
            tSum=base+i
            if tSum<limit:
                sum+=tSum
        base+=commonMultiple
    return sum
def dummy(limit, factors):
    sum=0
    for i in range(0,limit):
        addFlag=False
        for j in factors:
            if i % j == 0:
                addFlag=True
        if addFlag:
            sum+=i
    return sum
