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
def printTheirAlgorithm():
    print("If input vector is empty return result vector\n"
            "\n"
            "block_size = (n-1)! ['n' is the size of vector]"
            "\n"
            "Figure out which block k will lie in and select the first element of that block\n"
            "(this can be done by doing (k-1)/block_size)\n"
            "\n"
            "Append selected element to result vector and remove it from original input vector\n"
            "\n"
            "Deduce from k the blocks that are skipped i.e k = k - selected*block_size and goto step 1\n")

def printSOAlgorithm():#https://stackoverflow.com/questions/31216097/given-n-and-k-return-the-kth-permutation-sequence
    print("Break into sequence\n"
            "To generate these indices, go from right to left and divide k by 1! for the rightmost two places, then 2! then 3! then 4! etc, and then modulo the result with the number of possible indices in that position, which is 1 for the rightmost, 2 for the second-rightmost etc. You don't have to calculate the factorial each time because you can keep a running product.\n"
            "You can break out of the loop as soon as k divided by the factorial is zero, so you only have to compute factorials up until roughly the size of k multiplied by the last place in which k divided by the factorial is non-zero. If k is too large, you need to switch to BigIntegers.\n"
            "Once you have the indices it's pretty straightforward to use them to generate the permutation.\n"
            "For 3 items:\n"
            "  1:  0 0 0\n"
            "  2:  0 1 0\n"
            "  3:  1 0 0\n"
            "  4:  1 1 0\n"
            "  5:  2 0 0\n"
            "  6:  2 1 0\n"
            "\n\n"
            "For 4 items:\n"
            "  1:  0 0 0 0\n"
            "  2:  0 0 1 0\n"
            "  3:  0 1 0 0\n"
            "  4:  0 1 1 0\n"
            "  5:  0 2 0 0\n"
            "  6:  0 2 1 0\n"

            "  7:  1 0 0 0\n"
            "  8:  1 0 1 0\n"
            "  9:  1 1 0 0\n"
            "  10: 1 1 1 0\n"
            "  11: 1 2 0 0\n"
            "  12: 1 2 1 0\n"

            "  13: 2 0 0 0\n"
            "  14: 2 0 1 0\n"
            "  15: 2 1 0 0\n"
            "  16: 2 1 1 0\n"
            "  17: 2 2 0 0\n"
            "  18: 2 2 1 0\n"

            "  19: 3 0 0 0\n"
            "  20: 3 0 1 0\n"
            "  21: 3 1 0 0\n"
            "  22: 3 1 1 0\n"
            "  23: 3 2 0 0\n"
            "  24: 3 2 1 0\n")

def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n -1 )

def find_kth_permutation(v, k, result):
  print("v="+str(v)+" k="+str(k)+" result="+str(result))
  if not v:
    return result

  n = len(v)
  # count is number of permutations starting with first digit (selectable indexes or"block_size")
  count = factorial(n - 1)
  selected = (k - 1) // count
  print("  count="+str(count)+" selected="+str(selected))

  result += str(v[selected])
  del v[selected]
  k = k - (count * selected)
  result=find_kth_permutation(v, k, result)
  return result


#def MY_find_kth_permutation(v, k, result):
#  #TODO: Write - Your - Code
#  return result


def test_find_kth_permutation():
    testVector=[(([1,2,3],6),321)]
    testVector.append(((["1","2","3","4"],8),"2143"))
    testVector.append(((["1","2","3","4"],24),"4321"))
    testVector.append(((["1","2","3","4"],23),"4312"))
    for iter in testVector:
        expectation=iter[1]
        thisResult=""
        thisResult=find_kth_permutation(iter[0][0],iter[0][1],thisResult)
        if str(expectation)==thisResult:
            print("Pass.")
        else:
            print("FAIL!!!  Expected "+str(expectation)+" but received "+str(thisResult))
    return


#printQuestion()
test_find_kth_permutation()
