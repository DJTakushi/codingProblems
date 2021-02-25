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
  if n ==1:
      result=[['{','}']]
  else:
      result=print_all_braces(n-1)
      idx=0
      mySet=set()
      for iter in result:
          #add to front

          #clone=iter.copy()
          #clone.insert(0,'{')
          #clone.append('}')

          iter.append('{')
          iter.append('}')
          #result.insert(idx,clone)
          idx+=1

  return result

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

    for iter in testVector:
        expectation=iter[1]
        thisResult=""
        thisResult=print_all_braces(iter[0])
        listNo=0
        for thisList in expectation:
            elementNo=0
            for thisElement in thisList:
                if listNo >= len(thisResult):
                    print("Fail!!!  Result does not have "+str(listNo)+" lists!")
                    return
                else:
                    if elementNo >= len(thisResult[listNo]):
                        print("Fail!!!  Result ["+str(listNo)+"] does not have "+str(elementNo)+" items")
                        return
                    else:
                        if thisElement!=thisResult[listNo][elementNo]:
                            print("FAIL!!!\n"
                                    "  In listNo "+str(listNo)+" elementNo "+str(elementNo)+"\n"
                                    "  Expected "+str(thisElement)+"\n"
                                    "  Received "+str(thisResult[listNo][elementNo]))
                            return
                elementNo+=1
            listNo+=1
        print("Pass.")
    return
test_print_all_braces()
