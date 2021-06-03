import os,sys,unittest,importlib,testHelper
import dc21
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        cmm=dc21.classRoomManager([(30,75),(0,50),(0,150)])
        self.assertEqual(2,cmm.getClassRoomQuanity())
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
