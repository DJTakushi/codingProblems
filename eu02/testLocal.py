import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import eu02
        self.assertEqual(0,eu02.sumEvenFib(0))
        self.assertEqual(0,eu02.sumEvenFib(1))
        self.assertEqual(2,eu02.sumEvenFib(2))
        self.assertEqual(2,eu02.sumEvenFib(3))
        self.assertEqual(2,eu02.sumEvenFib(4))
        self.assertEqual(2,eu02.sumEvenFib(5))
        self.assertEqual(2,eu02.sumEvenFib(6))
        self.assertEqual(2,eu02.sumEvenFib(7))
        self.assertEqual(10,eu02.sumEvenFib(8))
        self.assertEqual(10,eu02.sumEvenFib(9))
        self.assertEqual(10,eu02.sumEvenFib(33))
        self.assertEqual(44,eu02.sumEvenFib(34))
        self.assertEqual(44,eu02.sumEvenFib(35))
        self.assertEqual(4613732,eu02.sumEvenFib(4000000))
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
