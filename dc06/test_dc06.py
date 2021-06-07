import os,sys,unittest,importlib
import dc06
from random import random
class myTest(unittest.TestCase):
    def testTakMemory(self):
        class dummyClass:
            def __init__(self,val):
                self.val = val
        myMemory = dc06.takMemory()
        for i in range(myMemory.blockSize):
            myVar = dummyClass(random())
            myVarAddress =myMemory.allocateNew(myVar)
            self.assertEqual(myVar,myMemory.dereferencePointer(myVarAddress))
            self.assertEqual(myVarAddress,myMemory.get_pointer(myVar))
        myVar = dummyClass("foo")
        self.assertEqual(dc06.takMemory.Null,myMemory.allocateNew(myVar))
        myMemory.clear()

    def testXListBig(self):
        myMemory = dc06.takMemory()
        myXList=dc06.xList()
        nodeList=list()
        for i in range(100):
            nodeList.append(myXList.add(i))
            c=0
            for j in nodeList:
                self.assertEqual(j,myXList.get(c))
                c+=1
        myMemory.clear()

    def testXListShort(self):
        myMemory = dc06.takMemory()

        myXList=dc06.xList()
        self.assertEqual((None,None),myXList.getLastTwo())
        self.assertEqual(None,myXList.get(0))
        self.assertEqual(None,myXList.get(1))

        node0=myXList.add(556)
        self.assertEqual((None,node0),myXList.getLastTwo())
        self.assertEqual(dc06.takMemory.Null,node0.both)
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(None,myXList.get(1))

        node1=myXList.add(762)
        self.assertEqual(dc06.takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(dc06.takMemory.Null^node0.pointer,node1.both)
        self.assertEqual((node0,node1),myXList.getLastTwo())
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(node1,myXList.get(1))
        self.assertEqual(None,myXList.get(2))

        node2=myXList.add(1270)
        self.assertEqual(dc06.takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(node0.pointer^node2.pointer,node1.both)
        self.assertEqual(node1.pointer^dc06.takMemory.Null,node2.both)
        self.assertEqual((node1,node2),myXList.getLastTwo())
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(node1,myXList.get(1))
        self.assertEqual(node2,myXList.get(2))
        self.assertEqual(None,myXList.get(3))

        node3=myXList.add(20)
        self.assertEqual(dc06.takMemory.Null^node1.pointer,node0.both)
        self.assertEqual(node0.pointer^node2.pointer,node1.both)
        self.assertEqual(node1.pointer^node3.pointer,node2.both)
        self.assertEqual(node2.pointer^dc06.takMemory.Null,node3.both)
        self.assertEqual((node2,node3),myXList.getLastTwo())
        self.assertEqual(node0,myXList.get(0))
        self.assertEqual(node1,myXList.get(1))
        self.assertEqual(node2,myXList.get(2))
        self.assertEqual(node3,myXList.get(3))
        self.assertEqual(None,myXList.get(4))
        myMemory.clear()
    def test_this(self):
        #self.testTakMemory()
        self.testXListBig()
        self.testXListShort()
if __name__=="__main__":
    unittest.main()
