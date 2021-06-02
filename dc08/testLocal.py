
import os,sys,unittest,importlib,testHelper
import dc08
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        headNode=dc08.node(0,dc08.node(1),dc08.node(0,dc08.node(1,dc08.node(1),dc08.node(1)),dc08.node(0)))
        self.assertEqual(5,dc08.univalCount(headNode))

        headNode=dc08.node(0,dc08.node(1),dc08.node(0))
        self.assertEqual(2,dc08.univalCount(headNode))

#   a
#  / \
# a   a
#     /\
#    a  a
#        \
#         A
        headNode=dc08.node('a',dc08.node('a'),dc08.node('a',dc08.node('a'),dc08.node('a',None,dc08.node('A'))))
        self.assertEqual(3,dc08.univalCount(headNode))

#   a
#  / \
# c   b
#     /\
#    b  b
#         \
#          b
        headNode=dc08.node('a',dc08.node('c'),dc08.node('b',dc08.node('b'),dc08.node('b',None,dc08.node('b'))))
        self.assertEqual(5,dc08.univalCount(headNode))

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
