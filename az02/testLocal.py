import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        class testCase:
            def __init__(self,arr,target,result):
                self.a = arr
                self.tgt = target
                self.result = result
        import az02
        testVector = []
        testVector.append(testCase([5,7,1,2,8,4,3], 10,True))
        testVector.append(testCase([5,7,1,2,8,4,3], 19,False))
        testVector.append(testCase([5,7,1,2,8,4,3,18], 19,True))

        for i in testVector:
            result = az02.find_sum_of_two(i.a,i.tgt)
            self.assertEqual(i.result,result)
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
