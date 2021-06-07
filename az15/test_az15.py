import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import az15
        class testCase:
            def __init__(self,arr,key,expectation):
                self.arr=arr
                self.key=key
                self.expectation = expectation
        def getTestVector():
            tar0=[1,10,20,47,59,63,75,88,99,107,120,133,155,162,176,188,199,200,210,222]
            testVector=list()
            counter=0
            for iter in tar0:
                testVector.append(testCase(tar0,iter,counter))
                counter+=1
            tar1=[176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
            counter=0
            for iter in tar1:
                testVector.append(testCase(tar1,iter,counter))
                counter+=1
            tar2=[47,59,63,75,88,99,107,120,133,155,162,176,188,199,200,210,222,1,10,20]
            counter=0
            for iter in tar2:
                testVector.append(testCase(tar2,iter,counter))
                counter+=1
            return testVector

        testVector = getTestVector()
        for i in testVector:
            self.assertEqual(i.expectation,az15.binary_search_rotated(i.arr,i.key))
if __name__=="__main__":
    unittest.main()
