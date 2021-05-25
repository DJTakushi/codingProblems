import os,sys,unittest
class myTest(unittest.TestCase):
    def testThis(self):
        #from az01solution import my_find_missing
        import az01solution
        testVector = []
        testVector.append((([3,7,1,2,8,4,5]),6))
        testVector.append((([3,7,1,2,8,4,5,10,9]),6))
        testVector.append((([3,7,1,2,8,4,5,10,9,12,6]),11))

        for i in testVector:
            result = az01solution.my_find_missing(i[0])
            self.assertEqual(i[1],result)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(myTest('testThis'))
    #suite.addTest(myTest('test_widget_resize'))
    return suite

def testSolution():
    runInStdOut=False
    if runInStdOut:
        runner = unittest.TextTestRunner()
        runner(stream=sys.stdout).run(suite())
    else:
        dirpath = os.path.dirname(os.path.abspath(__file__))
        testLogFilePath = dirpath+'/test.stdout.log'
        sys.stdout = open(testLogFilePath, "w")
        demo_test = unittest.TestLoader().loadTestsFromTestCase(myTest)
        unittest.TextTestRunner(stream=sys.stdout).run(demo_test)
        sys.stdout.close()
        sys.stdout = sys.__stdout__

        fileInput = open(testLogFilePath,"r")

        result = ""
        for i in fileInput.readlines():
            if "FAIL:" in i:
                result = "Fail"
        if "Fail" not in result:
            result = "Pass"
        return result
if __name__=="__main__":
    print(testSolution())
