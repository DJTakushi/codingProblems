def printProblem():
    print("If we list all the natural numbers below 10 that are multiples\n"
            "of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.\n"
            "Find the sum of all the multiples of 3 or 5 below 1000.")
def sumOfFactors(limit, factors):
    commonMultiple=1
    for i in factors: #could reduce this to use the LCM, but I can't now
        commonMultiple*=i
    addendSet=set()
    for i in factors:
        c=i
        while(c <= commonMultiple):
            addendSet.add(c)
            c+=i
    addendList=list(addendSet)
    addendList.sort() #may be probelmatic for very long lists
    base, sum = 0, 0
    while(base < limit):
        for i in addendList:
            tSum=base+i
            if tSum<limit:
                sum+=tSum
        base+=commonMultiple
    return sum
def dummy(limit, factors):
    sum=0
    for i in range(0,limit):
        addFlag=False
        for j in factors:
            if i % j == 0:
                addFlag=True
        if addFlag:
            sum+=i
    return sum
import unittest
import math
class UnitTest(unittest.TestCase):
    def test_myCases(self):
        self.assertEqual(5,sumOfFactors(10,[5]))
        self.assertEqual(45,sumOfFactors(10,[1]))
        self.assertEqual(23,sumOfFactors(10,[3,5]))
        self.assertEqual(dummy(1000,[3,5]),sumOfFactors(1000,[3,5]))
        self.assertEqual(dummy(5000,[3,5,2,3]),sumOfFactors(5000,[3,5,2,3]))
        self.assertEqual(dummy(5000,[3,5,2,3,93]),sumOfFactors(5000,[3,5,2,3,93]))
if __name__=='__main__':
    unittest.main()
