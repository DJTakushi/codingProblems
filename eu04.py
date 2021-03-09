def printProblem():
    print("A palindromic number reads the same both ways. The largest\n"
            "palindrome made from the product of two 2-digit numbers is\n"
            "  9009 = 91 × 99.\n"
            "Find the largest palindrome made from the product of two 3-digit\n"
            "numbers.")

def maxPalindrome(digits):
    #find all produts , put the in descending order, and check if they*re a palindrome
    #there must be a better way to do this.
    import math
    maxNum=int(math.pow(10,digits)-1)
    productSet=set()

    for i in range(1,maxNum+1):
        for j in range(1,maxNum+1):
            productSet.add(i*j)
    productList=list(productSet)
    productList.sort(reverse=True)
    for i in productList:
        if isPalindrome(i):
            return i
    return -1

def isPalindrome(input):
    arr=getDigitArray(input)
    lidx, hidx = 0, len(arr)-1
    while(lidx <= hidx):
        if(arr[lidx]!=arr[hidx]):
            return False
        lidx+=1
        hidx-=1
    return True
def getDigitArray(input):
    output=list()
    while input > 0:
        output.append(input%10)
        input//=10
    return output

import unittest
class UnitTest(unittest.TestCase):
    def testGetDigitArray(self):
        self.assertEqual([1],getDigitArray(1))
        self.assertEqual([2],getDigitArray(2))
        self.assertEqual([9],getDigitArray(9))
        self.assertEqual([0,1],getDigitArray(10))
        self.assertEqual([1,1],getDigitArray(11))
        self.assertEqual([8,9],getDigitArray(98))
        self.assertEqual([9,9],getDigitArray(99))
        self.assertEqual([0,0,1],getDigitArray(100))
        self.assertEqual([1,0,1],getDigitArray(101))
        self.assertEqual([8,9,9],getDigitArray(998))
        self.assertEqual([9,9,9],getDigitArray(999))
        self.assertEqual([0,0,0,1],getDigitArray(1000))
        self.assertEqual([1,0,0,1],getDigitArray(1001))
    def test_isPalindrome(self):
        self.assertEqual(True,isPalindrome(1))
        self.assertEqual(False,isPalindrome(10))
        self.assertEqual(True,isPalindrome(11))
        self.assertEqual(True,isPalindrome(99))
        self.assertEqual(True,isPalindrome(909))
        self.assertEqual(True,isPalindrome(9009))
        self.assertEqual(True,isPalindrome(90109))
        self.assertEqual(True,isPalindrome(906609))
        self.assertEqual(False,isPalindrome(906619))
    def test_myCases(self):
        self.assertEqual(9,maxPalindrome(1))
        self.assertEqual(9009,maxPalindrome(2))
        self.assertEqual(906609,maxPalindrome(3))
if __name__=='__main__':
    unittest.main()
