import os,sys,unittest,importlib,testHelper
import dc07
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(1,dc07.decode("2"))
        self.assertEqual(1,dc07.decode("1"))
        self.assertEqual(1,dc07.decode("3"))
        self.assertEqual(1,dc07.decode("4"))
        self.assertEqual(1,dc07.decode("5"))
        self.assertEqual(1,dc07.decode("6"))
        self.assertEqual(1,dc07.decode("7"))
        self.assertEqual(1,dc07.decode("8"))
        self.assertEqual(1,dc07.decode("9"))
        self.assertEqual(2,dc07.decode("10"))
        self.assertEqual(2,dc07.decode("11"))
        self.assertEqual(2,dc07.decode("12"))
        self.assertEqual(2,dc07.decode("13"))
        self.assertEqual(2,dc07.decode("14"))
        self.assertEqual(2,dc07.decode("15"))
        self.assertEqual(2,dc07.decode("16"))
        self.assertEqual(2,dc07.decode("17"))
        self.assertEqual(2,dc07.decode("18"))
        self.assertEqual(2,dc07.decode("19"))
        self.assertEqual(2,dc07.decode("20"))
        self.assertEqual(2,dc07.decode("21"))
        self.assertEqual(2,dc07.decode("22"))
        self.assertEqual(2,dc07.decode("23"))
        self.assertEqual(2,dc07.decode("24"))
        self.assertEqual(2,dc07.decode("25"))
        self.assertEqual(2,dc07.decode("26")) #b+f, z
        self.assertEqual(1,dc07.decode("27")) #b+f, z
        self.assertEqual(3,dc07.decode("111"))
        self.assertEqual(3,dc07.decode("126"))
        self.assertEqual(2,dc07.decode("127")) #1,2,7 , 12,7, 1,27 fails!

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
