import os,sys,unittest
def getTestLogPath():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    return dirpath+'/test.stdout.log'
def checkTestLog():
    fileInput = open(getTestLogPath(),"r")
    result = ""
    for i in fileInput.readlines():
        if "FAIL:" in i:
            result = "Fail"
        if "ERROR:" in i:
            result = "Error"
    if result == "":
        result = "Pass"
    return result
def testSolution(myTest):
    testLogFilePath = getTestLogPath()
    sys.stdout = open(testLogFilePath, "w")
    demo_test = unittest.TestLoader().loadTestsFromTestCase(myTest)
    unittest.TextTestRunner(stream=sys.stdout).run(demo_test)
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    return checkTestLog()
