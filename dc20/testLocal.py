import os,sys,unittest,importlib,testHelper
import dc20
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        nodeA=dc20.node(3,dc20.node(7,dc20.node(8,dc20.node(10))))
        nodeB=dc20.node(99,dc20.node(1,dc20.node(8,dc20.node(10))))
        self.assertEqual(8,dc20.findIntersect(nodeA,nodeB).val)
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
