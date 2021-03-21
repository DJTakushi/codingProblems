
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
    #return simpleMethod(input)
    sum,pIdx,ppIdx=input[0],0,-2 #default to take first
    for i in range(1,len(input)):
        if i - pIdx > 1: #add if possible
            sum+=input[i]
            ppIdx=pIdx
            pIdx=i
        else:
            potentialSum=sum-input[pIdx]
            potentialSum+=input[i]
            canUsePIdxM1=False
            if pIdx-1 >=0 and pIdx-1 !=ppIdx+1:
                canUsePIdxM1=True
                potentialSum+=input[pIdx-1]
            if potentialSum > sum:
                if canUsePIdxM1:
                    pIdx-=1
                    ppIdx = pIdx #pp unchanged
                pIdx = i
                sum=potentialSum
    return sum
def simpleMethod(input):
    #calculate each sum and check if it's the good.  If highest record, it's highest.  Completes in 2^n time
    class trial:
        def __init__(self,num,inputArray=None):
            self.num=num
            self.arrBin=list()
            for i in range(len(input)) :
                if num%2==1:
                    self.arrBin.append(True)
                else:
                    self.arrBin.append(False)
                num=num>>1
            self.valid=True
            for i in range(len(self.arrBin)):
                if i > 0:
                    if self.arrBin[i] and self.arrBin[i-1]:
                        self.valid=False
            if inputArray:
                self.getSum(inputArray)
            #self.printTrial()
        def printTrial(self):
            print("num = "+str(self.num))
            print("arrBin = "+str(self.arrBin))
            print("self.valid = "+str(self.valid))
        def getSum(self,inputArray):
            self.sum=0
            for i in range(len(self.arrBin)):
                if self.arrBin[i]:
                    self.sum+=inputArray[i]
    import math
    maxOption=math.pow(2,len(input))

    trialArray=list()
    maxSum = 0
    for i in range(int(maxOption)):
        thisTrial = trial(i,input)
        if thisTrial.valid and thisTrial.sum > maxSum:
            maxSum = thisTrial.sum
    return maxSum

import unittest
class myTestsClass(unittest.TestCase):
    def testThis(self):
        self.assertEqual(13,sumNonAdjNumbers([2,4,6,2,5]))
                                            # x   x   x
        self.assertEqual(10,sumNonAdjNumbers([5,1,1,5]))
                                            # x     x

        self.assertEqual(12,sumNonAdjNumbers([1,5,6,6,5,1]))
                                              # x   x   x
                                              #   x   x   x

        self.assertEqual(96,sumNonAdjNumbers([5,1,1,5,90]))
       #  idx val prevIdx  prevPrevIdx prevsum  prevPrevsum  sum
       # x0   5   None     None        None     None         0   all none.  Add
       #  1   1   0        None        0        0            5   can't add, so don't
       # x2   1   0        None        0        0            5   fine since last.  Add
       #  3   5   2        0           5        5            6   val+prevSum>sum.  Remove previous.  Check if prev-prev is affected.  Will not be.
       # x4   90  3        0           5        5            10  val+presum>sum.  Remove previous.  Check if prev-prev would effect taking what's before previous.  Does not.  Add it.

        self.assertEqual(100,sumNonAdjNumbers([5,1,1,5,0,90]))
                                              # x     x   x
        self.assertEqual(102,sumNonAdjNumbers([5,0,1,0,1,0,5,0,90]))
        self.assertEqual(101,sumNonAdjNumbers([5,1,1,5,0,90,91]))
        self.assertEqual(190,sumNonAdjNumbers([5,1,1,5,0,90,91,90]))
#
# compare by pairs (n,n+1) vs (n+1,n+2)
#     select which yields higher.  No, won't work for [5,1,1,5,0,90]

if __name__=="__main__":
    unittest.main()
