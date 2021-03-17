
def printProblem():
    print("Problem \#9 [Hard]\n"
          "This problem was asked by Airbnb.\n"
            "Given a list of integers, write a function that returns the\n"
             "largest sum of non-adjacent numbers. Numbers can be 0 or\n"
             "negative.\n"
             "For example, [2, 4, 6, 2, 5] should return 13, since we pick\n"
             "2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5\n"
             "and 5.\n"
             "Follow-up: Can you do this in O(N) time and constant space?")

def sumNonAdjNumbers(input):
    return -1
def simpleMethod(input):
    #calculate each sum and check if it's the good.  If highest record, it's highest.  Completes in 2^n time


import unittest
class myTestsClass(unittest.TestCase):
    def testThis(self):
        self.assertEqual(13,sumNonAdjNumbers([2,4,6,2,5]))
                                              x   x   x

        self.assertEqual(10,sumNonAdjNumbers([5,1,1,5]))
                                              x     x

        self.assertEqual(12,sumNonAdjNumbers([1,5,6,6,5,1]))
                                              x   x   x
                                                x   x   x

        self.assertEqual(96,sumNonAdjNumbers([5,1,1,5,90]))
                                              x   x   x
        idx val prevIdx  prevPrevIdx prevsum  prevPrevsum  sum
        0   5   None     None        None     None         0   all none.  Add
        1   1   0        None        0        0            5   can't add, so don't
        2   1   0        None        0        0            5   fine since last.  Add
        3   5   2        0           5        5            6   val+prevSum>sum.  Remove previous.  Check if prev-prev is affected.  Will not be.
        4   90  3        0           5        5            10  val+presum>sum.  Remove previous.  Check if prev-prev would effect taking what's before previous.  Does not.  Add it.

         self.assertEqual(100,sumNonAdjNumbers([5,1,1,5,0,90]))
                                                x     x   x

compare by pairs (n,n+1) vs (n+1,n+2)
    select which yields higher.  No, won't work for [5,1,1,5,0,90]

if __name__=="__main__":
    unittest.main()
