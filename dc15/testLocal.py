
import os,sys,unittest,importlib,testHelper
import dc15
from random import random
class myTest(unittest.TestCase):
    def test_this(self):

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
