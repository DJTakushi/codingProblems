import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import az08
        class myTestCase():
            def __init__(self,input,expected):
                self.input = input
                self.expected = expected
        tv=list()
        tv.append(myTestCase("World Hello","Hello World"))
        tv.append(myTestCase("To be or not to be","be to not or be To"))
        tv.append(myTestCase("You are amazing","amazing are You"))
        for i in tv:
            self.assertEqual(i.expected,az08.reverse_words(i.input))
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
