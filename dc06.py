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
    def getNewAddress():
        return int(takMemory.blockSize*random())
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
# [0]
# b=null
#
# [0]----------------[1]
# b=null^1.p       b=1.p^null
#
# [0]----------------[1]----------------[1]
# b=null^1.p       b=1.p^2.p         b=1.p^null
    headNode=None
    def __init__(self,val,prev=0,next=0):
        self.val=val
        if not xNode.headNode:
            xNode.headNode=self
        self.pointer = takMemory.allocateNew(self)
        self.both=takMemory.Null
    def add(element):
        lastNodes = xNode.getLastTwo()
        thisNode = xNode(element)
        if lastNodes[1]:
            if lastNodes[0]:
                lastNodes[1].both=lastNodes[0].pointer^thisNode.pointer #add new forward addr
            else:
                lastNodes[1].both^=thisNode.pointer #add new forward addr
            thisNode.both^=lastNodes[1].pointer #add previous addr to new node
        else:
            thisNode.both=takMemory.Null
        return thisNode
    def getLastTwo(): #will often need to get the last two to update the last
        nodeA=None
        nodeB=None
        if xNode.headNode:
            nodeB=xNode.headNode
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
    def get(idx):
        nodeA=None
        nodeB=None
        if xNode.headNode:
            nodeB=xNode.headNode
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
    def YtestBig(self):
        nodeList=list()
        for i in range(10):
            nodeList.append(xNode.add(i))
            c=0
            for j in nodeList:
                self.assertEqual(j,xNode.get(c))
                c+=1


    def testXnode(self):
        takMemory.clear()
        self.assertEqual((None,None),xNode.getLastTwo())
        self.assertEqual(None,xNode.get(0))
        self.assertEqual(None,xNode.get(1))

        node0=xNode.add(556)
        self.assertEqual((None,node0),xNode.getLastTwo())
        self.assertEqual(takMemory.Null,node0.both)
        self.assertEqual(node0,xNode.get(0))
        self.assertEqual(None,xNode.get(1))

        node1=xNode.add(762)
        self.assertEqual(takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(takMemory.Null^node0.pointer,node1.both)
        self.assertEqual((node0,node1),xNode.getLastTwo())
        self.assertEqual(node0,xNode.get(0))
        self.assertEqual(node1,xNode.get(1))
        self.assertEqual(None,xNode.get(2))

        node2=xNode.add(1270)
        self.assertEqual(takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(node0.pointer^node2.pointer,node1.both)
        self.assertEqual(node1.pointer^takMemory.Null,node2.both)
        self.assertEqual((node1,node2),xNode.getLastTwo())
        self.assertEqual(node0,xNode.get(0))
        self.assertEqual(node1,xNode.get(1))
        self.assertEqual(node2,xNode.get(2))
        self.assertEqual(None,xNode.get(3))

        node3=xNode.add(20)
        self.assertEqual(takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(node0.pointer^node2.pointer,node1.both)
        self.assertEqual(node1.pointer^node3.pointer,node2.both)
        self.assertEqual(node2.pointer^takMemory.Null,node3.both)
        self.assertEqual((node2,node3),xNode.getLastTwo())
        self.assertEqual(node0,xNode.get(0))
        self.assertEqual(node1,xNode.get(1))
        self.assertEqual(node2,xNode.get(2))
        self.assertEqual(node3,xNode.get(3))
        self.assertEqual(None,xNode.get(4))

if __name__=="__main__":
    unittest.main()
