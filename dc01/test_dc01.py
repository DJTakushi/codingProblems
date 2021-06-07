import os,sys,unittest,importlib
import dc01
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(True,dc01.canSumToKey([10,15,3,7],17))
        self.assertEqual(False,dc01.canSumToKey([10,15,3,8],17))
        self.assertEqual(True,dc01.canSumToKey([15,2,8],17))
        self.assertEqual(True,dc01.canSumToKey([15,2],17))
        self.assertEqual(True,dc01.canSumToKey([15,1,2,3,4,5,6,7,8],17))
        self.assertEqual(False,dc01.canSumToKey([0,2,4,6,8,10,12,14,16,18,20],17))
if __name__=="__main__":
    unittest.main()
