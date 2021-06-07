import os,sys,unittest,importlib
import dc14
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        myPi = dc14.getPiMonteCarlo(1000000)
        for i in range(10):#test this ten times for good measure.
            self.assertTrue(3.13 < myPi and myPi < 3.15)
if __name__=="__main__":
    unittest.main()
