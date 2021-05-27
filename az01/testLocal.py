import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        #from az01solution import my_find_missing
        import az01solution
        testVector = []
        testVector.append((([3,7,1,2,8,4,5]),6))
        testVector.append((([3,7,1,2,8,4,5,10,9]),6))
        testVector.append((([3,7,1,2,8,4,5,10,9,12,6]),11))

        for i in testVector:
            result = az01solution.my_find_missing(i[0])
            self.assertEqual(i[1],result)
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
