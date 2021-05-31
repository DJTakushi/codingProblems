import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import az12
        class myTestCase():
            def __init__(self,v,expected):
                self.v = v
                self.expected = expected
        tv=list()
        tv.append(myTestCase(1,{('{','}')}))
        tv.append(myTestCase(2,{('{','{','}','}'),('{','}','{','}')}))
        tv.append(myTestCase(3,{('{', '{', '{', '}', '}', '}'),('{', '{', '}', '{', '}', '}'),('{', '{', '}', '}', '{', '}'),('{', '}', '{', '{', '}', '}'),('{', '}', '{', '}', '{', '}')}))
        for i in tv:
            thisResult= az12.print_all_braces(i.v)
            self.assertEqual(i.expected,thisResult)
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
