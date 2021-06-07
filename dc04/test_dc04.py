import os,sys,unittest,importlib
import dc04
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(3,dc04.findMissingPositiveInteger([1,2,0]))
        self.assertEqual(2,dc04.findMissingPositiveInteger([3,4,-1,1]))
        self.assertEqual(1,dc04.findMissingPositiveInteger([3,3,-1,-2,3,3,2,4]))
        self.assertEqual(5,dc04.findMissingPositiveInteger([3,3,-1,-2,1,3,3,2,4]))
        self.assertEqual(6,dc04.findMissingPositiveInteger([1,2,3,4,5]))
        self.assertEqual(6,dc04.findMissingPositiveInteger([5,4,3,2,1]))
        self.assertEqual(19,dc04.findMissingPositiveInteger([20,18,-1,-50,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,-1]))
if __name__=="__main__":
    unittest.main()
