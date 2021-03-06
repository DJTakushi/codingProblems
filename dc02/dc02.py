# Easy appraoch is to calculate the big sum, and then for each index, divide by
# the current index's value.  Fast & efficient, but division is verboten.
# Good for proofing a kosher solution though.
def simpleton(a):
    product=1
    for iter in a:
        product*=iter
    output=list()
    for iter in a:
        output.append(int(product/iter))
    return output

#create a binary tree where all the base nodes are the input numbers
#calculate the products in the parent nodes
#iterate down the tree applying the products that aren't related to the end node
def prettyBoi(a):#O(n)
    headNode=createBinaryTree(len(a))  # create as a binary tree.
    treeList=getNodeList(headNode)      #put end nodes in list for easy access
    for i in range(len(a)):             #apply values from a
        treeList[i].val=a[i]
    applyTreeVals(headNode)             #apply products`
    outputs=list()
    applyOutVals(headNode)              #apply outVals down tree
    for i in range(len(a)):
        outputs.append(treeList[i].outVal)
    return outputs

class Node:#provided
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.outVal = None #output value
    def printNode(self):
        print("node: "+str(self)+"\n"
                "  val = "+str(self.val)+"\n"
                "  myParentDir = "+ self.myParentDir)
def getNodeList(node):
    nodeList=list()
    if node.left:
        leftList=getNodeList(node.left)
        leftList.extend(nodeList)
        nodeList=leftList
    if not node.left and not node.right:
        nodeList.append(node)
    if node.right:
        rightList=getNodeList(node.right)
        nodeList.extend(rightList)
    return nodeList
def applyTreeVals(node):
    left,right=1,1
    if node.left:
        left=applyTreeVals(node.left)
    if node.right:
        right=applyTreeVals(node.right)
    node.val*=left*right
    return node.val
def applyOutVals(node,pVal=1):
    LCVal, RCVal = 1,1
    if not node.left and not node.right:
        node.outVal=pVal
    else:
        applyOutVals(node.left,pVal*node.right.val)
        applyOutVals(node.right,pVal*node.left.val)
def createBinaryTree(nodeNum):
    if nodeNum==0:
        return

    baseLevel=0
    import math
    while(math.pow(2,baseLevel)<nodeNum):
        baseLevel+=1

    topArr, bottomArr=list(), list()
    headNode=Node(1)
    topArr.append(headNode)
    #nodeNum-=1
    lr="left"
    topPointer=0
    thisLevel=1
    while thisLevel <= baseLevel:
        newNode=Node(1)
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
            topArr=list(bottomArr)
            bottomArr = list()
            topPointer=0
            thisLevel+=1
    return headNode

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
