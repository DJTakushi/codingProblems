
import os,sys,unittest,importlib,testHelper
import dc18
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual([10,7,8,8],dc18.maxValOSubArray([10,5,2,7,8,7],3))

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
