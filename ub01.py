def printPrompt():
    print("Given an array of integers, return a new array such that\n"
            "each element at index i of the new array is the product of\n"
            "all the numbers in the original array except the one at i.\n"
            "For example, if our input was [1, 2, 3, 4, 5],\n"
            "the expected output would be [120, 60, 40, 30, 24].\n"
            "If our input was [3, 2, 1], the expected output would be [2, 3, 6].\n"
            "Follow-up: what if you can't use division?")

# Easy appraoch is to calculate the big sum, and then for each index, divide by
# the current index's value.
def simpleton(a):
    product=1
    for iter in a:
        product*=iter
    output=list()
    for iter in a:
        output.append(product/iter)
    return output

def prettyBoi(a):
    headNode=createBinaryTree(len(a))
    treeList=getNodeList(headNode)

class Node:#provided
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        self.myParentDir = None #direction of node from parent's direction
def getNodeList(node):
    nodeList=list()
    if node.left:
        leftList=getNodeList(node.left)
        leftList.extend(nodeList)
        nodeList=leftList
    nodeList.append(node)
    if node.right:
        rightList=getNodeList(node.right)
        nodeList.extend(rightList)
    return nodeList
def createBinaryTree(nodeNum):
    if nodeNum==0:
        return

    baseLevel=0
    import math
    while(math.pow(2,baseLevel)<nodeNum):
        baseLevel+=1

    topArr, bottomArr=list(), list()
    headNode=Node("")
    topArr.append(headNode)
    #nodeNum-=1
    lr="left"
    topPointer=0
    thisLevel=0
    while thisLevel <= baseLevel:
        newNode=Node("")
        bottomArr.append(newNode)
        parentNode=topArr[topPointer]
        newNode.parent=parentNode
        if lr=="left":
            parentNode.left=newNode
            newNode.myParentDir="left"
            lr="right"
        else:
            parentNode.right=newNode
            lr="left"
            newNode.myParentDir="right"
            topPointer+=1
        if topPointer==len(topArr):
            topArr=bottomArr.copy()
            bottomArr.clear()
            topPointer=0
            thisLevel+=1
    return headNode



import unittest
class UnitTest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual([120,60,40,30,24],simpleton([1,2,3,4,5]))
        self.assertEqual([2,3,6],simpleton([3,2,1]))
        self.assertEqual([2,3,6],prettyBoi([3,2,1]))

if __name__=='__main__':
    unittest.main()

#If we can't use division, we can perhaps organize it somehow as a tree?
#   0
# 1  5*6*7*8 *3*4 *2
# 2  5*6*7*8 *3*4 *1

# 3  5*6*7*8 *1*2 *4
# 4  5*6*7*8 *1*2 *3

# 5 1*2*3*4 *7*8 *6
# 6 1*2*3*4 *7*8 *5

# 7 1*2*3*4 *5*6 *8
# 8 1*2*3*4 *5*6 *7
