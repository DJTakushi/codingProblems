#https://www.dailycodingproblem.com/blog/unival-trees/
def printProblem():
    print("This problem was asked by Google.\n"
            "A unival tree (which stands for \"universal value\") is a tree\n"
            "where all nodes under it have the same value.  Given the root to\n"
            "a binary tree, count the number of unival subtrees.\n"
            "For example, the following tree has 5 unival subtrees:\n"
            "   0 \n"
            "  / \ \n"
            " 1   0 \n"
            "    / \ \n"
            "   1   0 \n"
            "  / \ \n"
            " 1   1 \n")
 #   0 \n"
 #  / \ \n"
 # 1   0 \n"

#   a
#  / \
# a   a
#     /\
#    a  a
#        \
#         A
# This tree has 3 unival subtrees: the two ‘a’ leaves and the one ‘A’ leaf. The ‘A’ leaf causes all its parents to not be counted as a unival tree, however.
#
#   a
#  / \
# c   b
#     /\
#    b  b
#         \
#          b
# This tree has 5 unival subtrees: the leaf at ‘c’, and every ‘b’.
def univalCount(headNode, val=None):
    count = 0
    headPotential=True

    if headNode.left:
        leftResult=univalCount(headNode.left)
        count+=abs(leftResult)
        if headNode.val != headNode.left.val and leftResult >= 0:
            headPotential=False
    if headNode.right:
        rightResult=univalCount(headNode.right)
        count+=abs(rightResult)
        if headNode.val != headNode.right.val and rightResult >= 0:
            headPotential=False
    if not headPotential:
        count*=-1
    return count


class node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left=left
        self.right=right
import unittest
class myTest(unittest.TestCase):
    def test_this(self):
        headNode=node(0,node(1),node(0,node(1,node(1),node(1)),node(0)))
        self.assertEqual(5,univalCount(headNode))
if __name__=="__main__":
    unittest.main()
