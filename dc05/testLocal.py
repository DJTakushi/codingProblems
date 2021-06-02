import os,sys,unittest,importlib,testHelper
import dc05
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(3,dc05.car(dc05.cons(3,4)))
        self.assertEqual(4,dc05.cdr(dc05.cons(3,4)))
        self.assertEqual(0,dc05.car(dc05.cons(0,"viking")))
        self.assertEqual("viking",dc05.cdr(dc05.cons(0,"viking")))

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
