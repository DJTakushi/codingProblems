import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import az16
        class testCase:
            def __init__(self,n,x,expectation):
                self.n=n
                self.x=x
                self.expectation = expectation
        testVector=list()
        testVector.append(testCase(1,[2,1],1))
        testVector.append(testCase(2,[2,1],2))
        testVector.append(testCase(3,[2,1],3))
        testVector.append(testCase(4,[2,1],5))

        for i in testVector:
            self.assertEqual(i.expectation,az16.staircasefinal(i.n,i.x))
if __name__=="__main__":
    unittest.main()
