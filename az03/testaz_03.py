import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import az03
        result = az03.merge_sorted([4,8,15,19],[7,9,10,16])
        self.assertEqual([4,7,8,9,10,15,16,19],result)
if __name__=="__main__":
    unittest.main()
