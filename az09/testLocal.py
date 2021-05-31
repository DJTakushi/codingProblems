import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import az09
        class myTestCase():
            def __init__(self,denominations,ammount,expected):
                self.denominations = denominations
                self.ammount = ammount
                self.expected = expected
        tv=list()
        tv.append(myTestCase([1,5,10],20,9))
        tv.append(myTestCase([1,5,2],7,6))
        for i in tv:
            result = az09.solve_coin_change(i.denominations,i.ammount)
            self.assertEqual(i.expected,result)

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
