import os,sys,unittest,importlib
import dc19
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(8,dc19.minCost([[1,2],[1,2],[1,2],[1,2],[10,2]]))
        self.assertEqual(8,dc19.minCost([[1,2,3],[1,2,3],[1,2,3],[1,2,3],[10,10,2]]))
if __name__=="__main__":
    unittest.main()
