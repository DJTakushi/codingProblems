def print_all_braces(n):
  result=set()
  myList=list()
  myList.append('{')
  result=bracesRecursive(n,myList,result)
  return result
def bracesRecursive(n,theList,theSet):
    #print(theList)
    #print(type(theList))
    curLen=len(theList)
    if curLen>(n*2):
        return theSet
    lCount=0
    rCount=0
    for iter in theList:
        if iter=='{':
            lCount+=1
        if iter=='}':
            rCount+=1
    if curLen==(n*2):
        if lCount==rCount:
            theListTuple=tuple(theList)
            if theListTuple not in theSet:
                theSet.add(theListTuple)
                # print("ADDED! "+ str(theListTuple))
    else:
        theList.append('{')
        theSet=bracesRecursive(n,list(theList),theSet)
        theList.pop(-1)
        if rCount < lCount:
            theList.append('}')
            theSet=bracesRecursive(n,list(theList),theSet)
    return theSet
