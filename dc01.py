def printProblem():
    print("This problem was recently asked by Google.\n"
        "Given a list of numbers and a number k, return whether any two numbers\n"
        "from the list add up to k.\n"
        "For example, given [10, 15, 3, 7] and k of 17, return true since \n"
        "10 + 7 is 17.\n"
        "Bonus: Can you do this in one pass?")

def canSumToKey(arr, key):
    sArr = arr.copy()
    sArr.sort()
    for i in range(len(sArr)):
        if sArr[i]>key: #first item is too large to be possible; all after fail
            return False
        for j in range(i,len(sArr)):
            if sArr[j] > key:#all after are too big
                continue
            sum=sArr[i]+sArr[j]
            if sum==key:
                return True
            if sum > key:
                continue
    return False

import unittest
class myTestClass(unittest.TestCase):
    def test_this(self):
        self.assertEqual(True,canSumToKey([10,15,3,7],17))
        self.assertEqual(False,canSumToKey([10,15,3,8],17))
        self.assertEqual(True,canSumToKey([15,2,8],17))
        self.assertEqual(True,canSumToKey([15,2],17))
        self.assertEqual(True,canSumToKey([15,1,2,3,4,5,6,7,8],17))
        self.assertEqual(False,canSumToKey([0,2,4,6,8,10,12,14,16,18,20],17))
if __name__=="__main__":
    unittest.main()
