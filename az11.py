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
  c=0 #counter
  maxC=pow(2,len(v))-1
  maxIndex=len(v)-1
  while c < maxC:
      tempC=c
      idx=0
      tempSet=set()
      while idx <= maxIndex:
          thisVal=pow(2,idx)
          if tempC-thisVal >=0:
              tempSet.add(True)
              tempC-=thisVal
          else:
              tempSet.add(False)
          idx+=1
      print(tempSet)
      c+=1
  return sets

def test_get_all_subsets():
    testVector=[([2,3,4],[{}, {2}, {3}, {2, 3}, {4}, {2, 4}, {3, 4}, {2, 3, 4}])]
    testVector.append(([2,5,7],[{}, {2}, {5}, {2, 5}, {7}, {2, 7}, {5, 7}, {2, 5, 7}]))
    for iter in testVector:
        expectation=iter[1]
        thisResult=[]
        thisResult=get_all_subsets(iter[0],thisResult)
        if str(expectation)==thisResult:
            print("Pass.")
        else:
            print("FAIL!!!  Expected "+str(expectation)+" but received "+str(thisResult))
    return

test_get_all_subsets()
