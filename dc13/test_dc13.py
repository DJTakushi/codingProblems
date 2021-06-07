import os,sys,unittest,importlib
import dc13
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(4,countUniqueChars("Danny"))
        self.assertEqual(6,countUniqueChars("Daniel"))
        self.assertEqual(4,countUniqueChars("Mississippi"))
        self.assertEqual(3,countUniqueChars("abcba"))

        self.assertEqual("bcb",maxStrWithKUnique("abcba",2))
        self.assertEqual("",maxStrWithKUnique("abcba",0))
        self.assertEqual("a",maxStrWithKUnique("abcba",1))
        self.assertEqual("abcba",maxStrWithKUnique("abcba",3))
        self.assertEqual("ississippi",maxStrWithKUnique("Mississippi",3))
if __name__=="__main__":
    unittest.main()
