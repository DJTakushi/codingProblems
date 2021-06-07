import os,sys,unittest,importlib
import dc09
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(13,dc09.sumNonAdjNumbers([2,4,6,2,5]))
                                            # x   x   x
        self.assertEqual(10,dc09.sumNonAdjNumbers([5,1,1,5]))
                                            # x     x

        self.assertEqual(12,dc09.sumNonAdjNumbers([1,5,6,6,5,1]))
                                              # x   x   x
                                              #   x   x   x

        self.assertEqual(96,dc09.sumNonAdjNumbers([5,1,1,5,90]))
       #  idx val prevIdx  prevPrevIdx prevsum  prevPrevsum  sum
       # x0   5   None     None        None     None         0   all none.  Add
       #  1   1   0        None        0        0            5   can't add, so don't
       # x2   1   0        None        0        0            5   fine since last.  Add
       #  3   5   2        0           5        5            6   val+prevSum>sum.  Remove previous.  Check if prev-prev is affected.  Will not be.
       # x4   90  3        0           5        5            10  val+presum>sum.  Remove previous.  Check if prev-prev would effect taking what's before previous.  Does not.  Add it.

        self.assertEqual(100,dc09.sumNonAdjNumbers([5,1,1,5,0,90]))
                                              # x     x   x
        self.assertEqual(102,dc09.sumNonAdjNumbers([5,0,1,0,1,0,5,0,90]))
        self.assertEqual(101,dc09.sumNonAdjNumbers([5,1,1,5,0,90,91]))
        self.assertEqual(190,dc09.sumNonAdjNumbers([5,1,1,5,0,90,91,90]))
#
# compare by pairs (n,n+1) vs (n+1,n+2)
#     select which yields higher.  No, won't work for [5,1,1,5,0,90]
if __name__=="__main__":
    unittest.main()
