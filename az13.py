#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def printPrompt():
    print("13. Clone a Directed Graph\n"
        "  Given the root node of a directed graph, clone this graph by \n"
        "  creating its deep copy so that the cloned graph has the same\n"
        "  vertices and edges as the original graph.")



class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []

def clone(root):
  return None    # return root

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
