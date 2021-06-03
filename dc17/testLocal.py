
import os,sys,unittest,importlib,testHelper
import dc17
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(32, dc17.maxFilePathLen("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())