def printProblem():
    print("Daily Coding Problem: Problem #20 [Easy]\n"
            "This problem was asked by Google.\n"
            "Given two singly linked lists that intersect at some point,\n"
            "find the intersecting node. The lists are non-cyclical.\n"
            "For example, given A = 3 -> 7 -> 8 -> 10 and\n"
            "B = 99 -> 1 -> 8 -> 10, return the node with value 8.\n"
            "In this example, assume nodes with the same value are the exact \n"
            "same node objects.\n"
            "Do this in O(M + N) time (where M and N are the lengths of the\n"
            "lists) and constant space.")

class node():
    def __init__(self,val, next=None):
        self.val=val
        self.n=next

def findIntersect(A,B):
    aValSet=set() #not actually constant space.  Could use a better hash or something
    while A:
        aValSet.add(A.val)
        A=A.n
    while B:
        if B.val in aValSet:
            return B
        B=B.n
    return -1

import unittest
class myTest(unittest.TestCase):
    def testThis(self):
        nodeA=node(3,node(7,node(8,node(10))))
        nodeB=node(99,node(1,node(8,node(10))))
        self.assertEqual(8,findIntersect(nodeA,nodeB).val)
if __name__=="__main__":
    unittest.main()
