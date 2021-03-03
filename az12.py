def print_all_braces(n):
  #TODO: Write - Your - Code
  hack=False
  if hack:
      result = []
      result.append(['{', '{', '{', '}', '}', '}'])
      result.append(['{', '{', '}', '{', '}', '}'])
      result.append(['{', '{', '}', '}', '{', '}'])
      result.append(['{', '}', '{', '{', '}', '}'])
      result.append(['{', '}', '{', '}', '{', '}'])
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
                print("ADDED! "+ str(theListTuple))
    else:
        theList.append('{')
        theSet=bracesRecursive(n,theList.copy(),theSet)
        theList.pop(-1)
        if rCount < lCount:
            theList.append('}')
            theSet=bracesRecursive(n,theList.copy(),theSet)
    return theSet

def test_print_all_braces():
    testVector=[
    ((1),[
    ['{','}']
    ])]
    testVector.append(
    ((2),[
    ['{','{','}','}'],#enclose 0
    ['{','}','{','}']#+R 0
    ]))               #+L is a duplicate
    testVector.append(
    ((3),[
    ['{', '{', '{', '}', '}', '}'],#enclose 0
    ['{', '{', '}', '{', '}', '}'],#enclose 1
    ['{', '{', '}', '}', '{', '}'],#+R 0
    ['{', '}', '{', '{', '}', '}'],#+L 0
    ['{', '}', '{', '}', '{', '}']]))#+R 1
                                     #+L 1 would be a dulicate
    for case in testVector:
        expectation=case[1]
        thisResult=set()
        thisResult=print_all_braces(case[0])
        testSet=set()
        for iter in expectation:
            thisTuple=tuple(iter)
            testSet.add(thisTuple)
        print(testSet)
        for iter in testSet:
            testTuple=tuple(iter)
            if testTuple not in thisResult:
                print("Fail!!!  Result does not have "+str(testTuple)+" !")
                return
            else:
                if len(testSet) != len(thisResult):
                    print("Fail!!!  Result expectd to have "+str(len(testSet))+" lists but returned "+str(len(thisResult))+" lists!")
                    return
        print("Pass ";0)

    return
test_print_all_braces()
