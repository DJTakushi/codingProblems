
import os,sys,unittest,importlib,testHelper
import dc22
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        wordList = ['quick', 'brown', 'the','fox']
        cStr="thequickbrownfox"
        expectation=['the','quick','brown','fox']
        self.assertEqual(expectation,dc22.stringToWordList(wordList,cStr))

        wordList=['the','theatre']
        cStr='theatre'
        expectation=['theatre']
        self.assertEqual(expectation,dc22.stringToWordList(wordList,cStr))
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
