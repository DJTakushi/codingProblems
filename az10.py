#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def printQuestion():
    print( "10.  Given a set of ‘n’ elements, find their Kth permutation.\n"
            "       Consider the following set of elements:\n"
            "           [1,2,3]\n"
            "           All permutations of the above elements are (with ordering):\n"
            "           1: [1,2,3]\n"
            "           2: [1,3,2]\n"
            "           3: [2,1,3]\n"
            "           4: [2,3,1]\n"
            "           5: [3,1,2]\n"
            "           6: [3,2,1]\n"
            "       Here we need to find the Kth permutation.\n"
            "       Runtime Complexity: Linear, O(n)\n"
            "       Memory Complexity: Linear, O(n)")
def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
  if not v:
    return

  n = len(v)
  # count is number of permutations starting with first digit
  count = factorial(n - 1)
  selected = (k - 1) // count

  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  find_kth_permutation(v, k, result)

def MY_find_kth_permutation(v, k, result):
  #TODO: Write - Your - Code
  return result


def test_find_kth_permutation():
    testVector=[(([1,2,3],6),321)]
    #testVector.append(((["1","2","3","4"],8),"2143"))
    for iter in testVector:
        expectation=iter[1]
        result=""
        result=find_kth_permutation(iter[0][0],iter[0][1],result)
        if expectation==result:
            print("Pass.")
        else:
            print("FAIL!!!  Expected "+str(expectation)+" but received "+str(result))
    return


#printQuestion()
test_find_kth_permutation()
