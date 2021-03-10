
def printProblem():
    print("This problem was asked by Stripe.\n"
            "  Given an array of integers, find the first missing positive\n"
            "  integer in linear time and constant space. In other words,\n"
            "  find the lowest positive integer that does not exist in the\n"
            "  array. The array can contain duplicates and negative numbers\n"
            "  as well.\n"
            "  For example, the input [3, 4, -1, 1] should give 2.\n"
            "  The input [1, 2, 0] should give 3.\n"
            "  You can modify the input array in-place.")
def myFunction(a):
    return -1

import unittest
class myTest(unittest.TestCase):
    def testThese(self):
        self.assertEqual(3,myFunction([1,2,0]))
        self.assertEqual(2,myFunction([3,4,-1,1]))
if __name__ == "__main__":
    unittest.main()
