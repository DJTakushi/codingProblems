import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import az14
        class testCase:
            def __init__(self,arr=list(),key=0,low=0,high=0):
                self.arr=arr
                self.key=key
                self.low=low
                self.high=high

        tar0=[1,2,5,5,5,5,5,5,5,5,20]
        testVector=list()
        testVector.append(testCase(tar0,1,0,0))
        testVector.append(testCase(tar0,2,1,1))
        testVector.append(testCase(tar0,5,2,9))
        testVector.append(testCase(tar0,20,10,10))
        tar1=[1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,6,6]
        testVector.append(testCase(tar1,1,0,2))
        testVector.append(testCase(tar1,2,3,7))
        testVector.append(testCase(tar1,3,8,10))
        testVector.append(testCase(tar1,4,11,14))
        testVector.append(testCase(tar1,5,15,17))
        testVector.append(testCase(tar1,6,18,23))
        testVector.append(testCase(tar1,8,-1,-1))
        for test in testVector:
            resultLow=az14.find_low_index(test.arr,test.key)
            resultHigh=az14.find_high_index(test.arr,test.key)
            failFlag=False
            self.assertEqual(test.low, resultLow)
            self.assertEqual(test.high, resultHigh)

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
