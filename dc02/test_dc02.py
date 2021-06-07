import os,sys,unittest,importlib
import dc02
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual([2,3,6],dc02.simpleton([3,2,1]))
        self.assertEqual([120,60,40,30,24],dc02.simpleton([1,2,3,4,5]))
        self.assertEqual([2,3,6],dc02.prettyBoi([3,2,1]))
        self.assertEqual([120,60,40,30,24],dc02.prettyBoi([1,2,3,4,5]))
        self.assertEqual(dc02.simpleton([9,5,7,22,45,12,57,19,365]),dc02.prettyBoi([9,5,7,22,45,12,57,19,365]))
        dArr=[1,2,3,4,5,6,7,8,9]
        self.assertEqual(dc02.simpleton(dArr),dc02.prettyBoi(dArr))
        dArr=[22,9,45,556,762,65,68,308,300,50]
        self.assertEqual(dc02.simpleton(dArr),dc02.prettyBoi(dArr))
if __name__=="__main__":
    unittest.main()
