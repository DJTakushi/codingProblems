def printProblem():
    print("Daily Coding Problem: Problem #18 [Hard]\n"
            "This problem was asked by Google.\n"
            "Given an array of integers and a number k, where 1 <= k <= length\n"
            "of the array, compute the maximum values of each subarray of\n"
            "length k.\n"
            "For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we\n"
            "should get: [10, 7, 8, 8], since:\n"
            "  10 = max(10, 5, 2)\n"
            "  7 = max(5, 2, 7)\n"
            "  8 = max(2, 7, 8)\n"
            "  8 = max(7, 8, 7)\n"
            "Do this in O(n) time and O(k) space. You can modify the input\n"
            "array in-place and you do not need to store the results. You can\n"
            "simply print them out as you compute them.")
def maxValOSubArray(ar, k):
    out=list()
    for i in range(len(ar)+1-k):
        out.append(max(ar[i:i+k])) #this operates at O(k) though
    return out

def maxValOSubArrayFAST(ar, k):
    # preserve the current max
    # replace it if
    #     the next entered one is the new max
    #     OR it has expired
    #         Will then have to recompute with O(k) though
    return -1

import unittest
class myTest(unittest.TestCase):
    def testThis(self):
        self.assertEqual([10,7,8,8],maxValOSubArray([10,5,2,7,8,7],3))
if __name__=="__main__":
    unittest.main()
