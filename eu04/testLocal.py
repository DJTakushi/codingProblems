import os,sys,unittest,importlib,testHelper
import eu04
class myTest(unittest.TestCase):
    def testgetDigitArray(self):
        self.assertEqual([1],eu04.getDigitArray(1))
        self.assertEqual([2],eu04.getDigitArray(2))
        self.assertEqual([9],eu04.getDigitArray(9))
        self.assertEqual([0,1],eu04.getDigitArray(10))
        self.assertEqual([1,1],eu04.getDigitArray(11))
        self.assertEqual([8,9],eu04.getDigitArray(98))
        self.assertEqual([9,9],eu04.getDigitArray(99))
        self.assertEqual([0,0,1],eu04.getDigitArray(100))
        self.assertEqual([1,0,1],eu04.getDigitArray(101))
        self.assertEqual([8,9,9],eu04.getDigitArray(998))
        self.assertEqual([9,9,9],eu04.getDigitArray(999))
        self.assertEqual([0,0,0,1],eu04.getDigitArray(1000))
        self.assertEqual([1,0,0,1],eu04.getDigitArray(1001))
    def test_isPalindrome(self):
        self.assertEqual(True,eu04.isPalindrome(1))
        self.assertEqual(False,eu04.isPalindrome(10))
        self.assertEqual(True,eu04.isPalindrome(11))
        self.assertEqual(True,eu04.isPalindrome(99))
        self.assertEqual(True,eu04.isPalindrome(909))
        self.assertEqual(True,eu04.isPalindrome(9009))
        self.assertEqual(True,eu04.isPalindrome(90109))
        self.assertEqual(True,eu04.isPalindrome(906609))
        self.assertEqual(False,eu04.isPalindrome(906619))
    def test_myCases(self):
        self.assertEqual(9,eu04.maxPalindrome(1))
        self.assertEqual(9009,eu04.maxPalindrome(2))
        self.assertEqual(906609,eu04.maxPalindrome(3))
    def testThis(self):
        self.testgetDigitArray()
        self.test_isPalindrome()
        self.test_myCases()

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
