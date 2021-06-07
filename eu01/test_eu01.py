import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import eu01
        self.assertEqual(5,eu01.sumOfFactors(10,[5]))
        self.assertEqual(45,eu01.sumOfFactors(10,[1]))
        self.assertEqual(23,eu01.sumOfFactors(10,[3,5]))
        self.assertEqual(eu01.dummy(1000,[3,5]),eu01.sumOfFactors(1000,[3,5]))
        self.assertEqual(eu01.dummy(5000,[3,5,2,3]),eu01.sumOfFactors(5000,[3,5,2,3]))
        self.assertEqual(eu01.dummy(5000,[3,5,2,3,93]),eu01.sumOfFactors(5000,[3,5,2,3,93]))
if __name__=="__main__":
    unittest.main()
