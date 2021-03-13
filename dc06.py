def printProblem():
    print("This problem was asked by Google.\n"
            "An XOR linked list is a more memory efficient doubly linked\n"
            "list. Instead of each node holding next and prev fields, it\n"
            "holds a field named both, which is an XOR of the next node and\n"
            "the previous node. Implement an XOR linked list; it has an\n"
            "add(element) which adds the element to the end, and a get(index)\n"
            "which returns the node at index.\n"
            "If using a language that has no pointers (such as Python), you\n"
            "can assume you have access to get_pointer and\n"
            "dereference_pointer functions that converts between nodes and\n"
            "memory addresses.")
from random import seed
from random import random
seed(1)
class takMemory:
    blockSize=1000
    takMemoryDict=dict()
    takMemorySet=set()
    Null=5150
    top=0
    USE_RANDOM_ADDRESSES = False
    def getNewAddress():
        if takMemory.USE_RANDOM_ADDRESSES:
            return int(takMemory.blockSize*random())
        else:
            takMemory.top+=1
            return takMemory.top-1

    def allocateNew(item):
        if len(takMemory.takMemorySet) >= takMemory.blockSize:
            return takMemory.Null
        thisAddress=takMemory.getNewAddress()
        while thisAddress in takMemory.takMemorySet:
            thisAddress=takMemory.getNewAddress()
        takMemory.takMemoryDict[thisAddress]=item
        takMemory.takMemorySet.add(thisAddress)
        return thisAddress
    def get_pointer(item):
        valList = list(takMemory.takMemoryDict.values())
        if item in valList:
            pos = valList.index(item)
            keyList = list(takMemory.takMemoryDict.keys())
            return keyList[pos]
        else:
            return takMemory.Null
    def dereferencePointer(address):
        if address in takMemory.takMemoryDict:
            return takMemory.takMemoryDict[address]
        else:
            return takMemory.Null
    def clear():
        takMemory.takMemoryDict.clear()
        takMemory.takMemorySet.clear()


class xNode:
    def __init__(self,val,prev=0,next=0):
        self.val=val
        self.pointer = takMemory.allocateNew(self)
        self.both=takMemory.Null

class xList:
# [0]
# b=null
#
# [0]----------------[1]
# b=null^1.p       b=1.p^null
#
# [0]----------------[1]----------------[1]
# b=null^1.p       b=1.p^2.p         b=1.p^null
    def __init__(self):
        self.headNode=None
    def add(self,element):
        lastNodes = self.getLastTwo()
        thisNode = xNode(element)
        if not self.headNode:
            self.headNode=thisNode
        if lastNodes[1]:
            if lastNodes[0]:
                lastNodes[1].both=lastNodes[0].pointer^thisNode.pointer #add new forward addr
            else:
                lastNodes[1].both^=thisNode.pointer #add new forward addr
            thisNode.both^=lastNodes[1].pointer #add previous addr to new node
        else:
            thisNode.both=takMemory.Null
        return thisNode
    def getLastTwo(self): #will often need to get the last two to update the last
        nodeA=None
        nodeB=None
        if self.headNode:
            nodeB=self.headNode
        else:
            return (None,None)
        while(True):
            nextAddr=takMemory.Null
            if nodeA:
                nextAddr = nodeB.both^nodeA.pointer
            else:
                if (nodeB.both==takMemory.Null):
                    return(nodeA,nodeB)
                nextAddr = nodeB.both^takMemory.Null
            if nextAddr != takMemory.Null: #nextAddr
                 nodeA=nodeB
                 nodeB=takMemory.dereferencePointer(nextAddr)
            else:
                return (nodeA,nodeB)
    def get(self,idx):
        nodeA=None
        nodeB=None
        if self.headNode:
            nodeB=self.headNode
        else:
            return None
        while(idx):
            nextAddr=takMemory.Null
            if nodeA:
                nextAddr = nodeB.both^nodeA.pointer
            else:
                if (nodeB.both==takMemory.Null):
                    return None
                nextAddr = nodeB.both^takMemory.Null
            if nextAddr != takMemory.Null: #nextAddr
                 nodeA=nodeB
                 nodeB=takMemory.dereferencePointer(nextAddr)
            else:
                return None
            idx-=1
        return nodeB
import unittest
class addrTest(unittest.TestCase):
    def testTakMemory(self):
        class dummyClass:
            def __init__(self,val):
                self.val = val
        for i in range(takMemory.blockSize):
            myVar = dummyClass(random())
            myVarAddress =takMemory.allocateNew(myVar)
            self.assertEqual(myVar,takMemory.dereferencePointer(myVarAddress))
            self.assertEqual(myVarAddress,takMemory.get_pointer(myVar))
        myVar = dummyClass("foo")
        self.assertEqual(takMemory.Null,takMemory.allocateNew(myVar))
        takMemory.clear()
class xNodeTest(unittest.TestCase):
    def testXListBig(self):
        takMemory.clear()
        myXList=xList()
        nodeList=list()
        for i in range(100):
            nodeList.append(myXList.add(i))
            c=0
            for j in nodeList:
                self.assertEqual(j,myXList.get(c))
                c+=1

    def testXListShort(self):
        myXList=xList()
        takMemory.clear()
        self.assertEqual((None,None),myXList.getLastTwo())
        self.assertEqual(None,myXList.get(0))
        self.assertEqual(None,myXList.get(1))

        node0=myXList.add(556)
        self.assertEqual((None,node0),myXList.getLastTwo())
        self.assertEqual(takMemory.Null,node0.both)
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(None,myXList.get(1))

        node1=myXList.add(762)
        self.assertEqual(takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(takMemory.Null^node0.pointer,node1.both)
        self.assertEqual((node0,node1),myXList.getLastTwo())
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(node1,myXList.get(1))
        self.assertEqual(None,myXList.get(2))

        node2=myXList.add(1270)
        self.assertEqual(takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(node0.pointer^node2.pointer,node1.both)
        self.assertEqual(node1.pointer^takMemory.Null,node2.both)
        self.assertEqual((node1,node2),myXList.getLastTwo())
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(node1,myXList.get(1))
        self.assertEqual(node2,myXList.get(2))
        self.assertEqual(None,myXList.get(3))

        node3=myXList.add(20)
        self.assertEqual(takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(node0.pointer^node2.pointer,node1.both)
        self.assertEqual(node1.pointer^node3.pointer,node2.both)
        self.assertEqual(node2.pointer^takMemory.Null,node3.both)
        self.assertEqual((node2,node3),myXList.getLastTwo())
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(node1,myXList.get(1))
        self.assertEqual(node2,myXList.get(2))
        self.assertEqual(node3,myXList.get(3))
        self.assertEqual(None,myXList.get(4))

if __name__=="__main__":
    unittest.main()
