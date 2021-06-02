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
    def getNewAddress(self):
        if takMemory.USE_RANDOM_ADDRESSES:
            return int(takMemory.blockSize*random())
        else:
            takMemory.top+=1
            return takMemory.top-1

    def allocateNew(self,item):
        if len(self.takMemorySet) >= self.blockSize:
            return takMemory.Null
        thisAddress=self.getNewAddress()
        while thisAddress in self.takMemorySet:
            thisAddress=self.getNewAddress()
        self.takMemoryDict[thisAddress]=item
        self.takMemorySet.add(thisAddress)
        return thisAddress
    def get_pointer(self,item):
        valList = list(takMemory.takMemoryDict.values())
        if item in valList:
            pos = valList.index(item)
            keyList = list(takMemory.takMemoryDict.keys())
            return keyList[pos]
        else:
            return takMemory.Null
    def dereferencePointer(self, address):
        if address in takMemory.takMemoryDict:
            return takMemory.takMemoryDict[address]
        else:
            return takMemory.Null
    def clear(self):
        takMemory.takMemoryDict.clear()
        takMemory.takMemorySet.clear()


class xNode:
    def __init__(self,val,mm,prev=0,next=0):
        self.val=val
        self.pointer = mm.allocateNew(self)
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
    def __init__(self,memoryManager=None):
        self.headNode=None
        if memoryManager:
            self.myMM = memoryManager
        else:
            self.myMM = takMemory()
    def add(self,element):
        lastNodes = self.getLastTwo()
        thisNode = xNode(element,self.myMM)
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
                 nodeB=self.myMM.dereferencePointer(nextAddr)
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
                 nodeB=self.myMM.dereferencePointer(nextAddr)
            else:
                return None
            idx-=1
        return nodeB
