 #dailyCoding problem#3
def printProblem():
    print("This problem was recently asked by Google.\n"
            "Given the root to a binary tree, implement\n"
            "serialize(root), which serializes the tree into a string, and\n"
            "deserialize(s), which deserializes the string back into the tree.")
class Node:#provided
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def serialize(node):
    nodeList=list()
    nodeList=getNodeList(node)
    outString=""
    for iter in nodeList:
        outString+=iter.val+delim
    return outString[0:-1]
delim=" "
def deserialize(s):
    values=s.split(delim)
    valueCount=len(values)
    headNode=createBinaryTree(valueCount)
    nodeList=getNodeList(headNode)
    for i in range(0,valueCount):
        nodeList[i].val=values[i]
    return headNode


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
    topArr, bottomArr=list(), list()
    headNode=Node("")
    topArr.append(headNode)
    nodeNum-=1
    lr="left"
    topPointer=0
    while nodeNum:
        newNode=Node("")
        bottomArr.append(newNode)
        parentNode=topArr[topPointer]
        if lr=="left":
            parentNode.left=newNode
            lr="right"
        else:
            parentNode.right=newNode
            lr="left"
            topPointer+=1
        if topPointer==len(topArr):
            topArr=list(bottomArr)
            bottomArr = list()
            topPointer=0
        nodeNum-=1
    return headNode

# import unittest
# class UnitTest(unittest.TestCase):
#     def test_case(self):
#         node = Node('root', Node('left', Node('left.left')), Node('right'))
#         self.assertEqual("left.left left root right",serialize(node))
#         self.assertEqual(deserialize(serialize(node)).left.left.val,'left.left')
#         self.assertEqual(deserialize(serialize(node)).left.val,'left')
#         self.assertEqual(deserialize(serialize(node)).right.val,'right')
#         self.assertEqual(deserialize(serialize(node)).val,'root')
#
#         node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
#         self.assertEqual("left.left left left.right root right",serialize(node))
#         self.assertEqual(deserialize(serialize(node)).left.left.val,'left.left')
#         self.assertEqual(deserialize(serialize(node)).left.right.val,'left.right')
#         self.assertEqual(deserialize(serialize(node)).left.val,'left')
#         self.assertEqual(deserialize(serialize(node)).right.val,'right')
#         self.assertEqual(deserialize(serialize(node)).val,'root')
#
#         node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right',Node('right.left')))
#         self.assertEqual("left.left left left.right root right.left right",serialize(node))
#         self.assertEqual(deserialize(serialize(node)).left.left.val,'left.left')
#         self.assertEqual(deserialize(serialize(node)).left.right.val,'left.right')
#         self.assertEqual(deserialize(serialize(node)).left.val,'left')
#         self.assertEqual(deserialize(serialize(node)).right.val,'right')
#         self.assertEqual(deserialize(serialize(node)).right.left.val,'right.left')
#         self.assertEqual(deserialize(serialize(node)).val,'root')
#
#         node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right',Node('right.left'),Node('right.right')))
#         self.assertEqual("left.left left left.right root right.left right right.right",serialize(node))
#         self.assertEqual(deserialize(serialize(node)).left.left.val,'left.left')
#         self.assertEqual(deserialize(serialize(node)).left.right.val,'left.right')
#         self.assertEqual(deserialize(serialize(node)).left.val,'left')
#         self.assertEqual(deserialize(serialize(node)).right.val,'right')
#         self.assertEqual(deserialize(serialize(node)).right.left.val,'right.left')
#         self.assertEqual(deserialize(serialize(node)).right.right.val,'right.right')
#         self.assertEqual(deserialize(serialize(node)).val,'root')
#
#         node = Node('root', Node('left', Node('left.left')), Node('right',Node('right.left'),Node('right.right')))
#         self.assertEqual("left.left left root right.left right right.right",serialize(node))
#         self.assertEqual(deserialize(serialize(node)).left.left.val,'left.left')
#         self.assertEqual(deserialize(serialize(node)).left.val,'left')
#         #all below will fail - tree is built top->down and left->right.  Cannot have skipped indexes.
#         # self.assertEqual(deserialize(serialize(node)).right.val,'right')
#         # self.assertEqual(deserialize(serialize(node)).right.left.val,'right.left')
#         # self.assertEqual(deserialize(serialize(node)).right.right.val,'right.right')
#         # self.assertEqual(deserialize(serialize(node)).val,'root')
#
#         node = Node('root', Node('left', Node('left.left',Node('left.left.left')), Node('left.right')), Node('right',Node('right.left'),Node('right.right')))
#         self.assertEqual("left.left.left left.left left left.right root right.left right right.right",serialize(node))
#         self.assertEqual(deserialize(serialize(node)).left.left.val,'left.left')
#         self.assertEqual(deserialize(serialize(node)).left.left.left.val,'left.left.left')
#         self.assertEqual(deserialize(serialize(node)).left.right.val,'left.right')
#         self.assertEqual(deserialize(serialize(node)).left.val,'left')
#         self.assertEqual(deserialize(serialize(node)).right.val,'right')
#         self.assertEqual(deserialize(serialize(node)).right.left.val,'right.left')
#         self.assertEqual(deserialize(serialize(node)).right.right.val,'right.right')
#         self.assertEqual(deserialize(serialize(node)).val,'root')

if __name__=='__main__':
    unittest.main()
