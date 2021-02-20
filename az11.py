#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def printQuestion():
    print( "11.  Find all subsets of a given set of integers\n"
            "           [1,2,3]\n"
            "       We are given a set of integers and we have to find all the \n"
            "       possible subsets of this set of integers. The following \n"
            "       example elaborates on this further\n"
            "       Given the set of intergers:\n"
            "         [2,3,4]\n"
            "       All possile subsets for the given set of integers:\n"
            "        [],[2],[3],[2,3],[4],[2,4],[3,4],[2,3,4]\n"
            "      Runtime Complexity: Exponential, O(2^n*n)\n"
            "      Memory Complexity: Exponential, O(2^n*n)")

def get_all_subsets(v, sets):
  #v = list of elements
  #set = list of sets
  maxIndex=len(v)-1
  pow2=[]
  c=0
  while c <= maxIndex:
      pow2.append(pow(2,c))
      c+=1
  number=0
  listOLists=[]
  while number <= pow(2,maxIndex+1)-1:
      tempNumber=number
      idx=maxIndex
      myList=[]
      while idx >=0:
          difference=tempNumber-pow2[idx]
          #print("  number="+str(number)+" tempNumber="+str(tempNumber)+" difference="+str(difference))
          if difference >=0:
              myList.insert(0,True)
              tempNumber-=pow2[idx]
          else:
              myList.insert(0,False)
          idx-=1
      #print("number="+str(number)+" myList="+str(myList))
      listOLists.append(myList)
      number+=1
  for thisList in listOLists:
      thisSet=set()
      c=0
      for iter in thisList:
          if iter:
              thisSet.add(v[c])
          c+=1
      sets.append(thisSet)
  return sets

def test_get_all_subsets():
    testVector=[([2,3,4],[set(), {2}, {3}, {2, 3}, {4}, {2, 4}, {3, 4}, {2, 3, 4}])]
    testVector.append(([2,5,7],[set(), {2}, {5}, {2, 5}, {7}, {2, 7}, {5, 7}, {2, 5, 7}]))
    for iter in testVector:
        expectation=iter[1]
        thisResult=[]
        thisResult=get_all_subsets(iter[0],thisResult)
        if len(expectation)==len(thisResult):
            c=0
            while c < len(expectation):
                if expectation[c]!=thisResult[c]:
                    print("FAIL!!!  Element "+str(c)+" should be "+str(expectation[c])+" but received "+str(thisResult[c]))
                c+=1
            print("Pass.")
        else:
            print("FAIL!!!  Expected list of lenth "+str(len(expectation))+" but received list of length "+str(len(thisResult)))
    return

test_get_all_subsets()
