import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import az07
        class myTestCase():
            def __init__(self,s,dictionary,expected):
                self.s = s
                self.dictionary = dictionary
                self.expected = expected
        tv=list()
        dict={"apple","apple","pear","pie"}
        tv.append(myTestCase("applepie",dict,True))
        tv.append(myTestCase("applepeer",dict,False))
        dict={"peach","apple","pear","pie"}
        tv.append(myTestCase("applepie",dict,True))
        tv.append(myTestCase("applepeer",dict,False))
        dict={"hell","now","on","hello"}
        tv.append(myTestCase("hellonow",dict,True))

        for i in tv:
            self.assertEqual(i.expected,az07.can_segment_string(i.s,i.dictionary))
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
