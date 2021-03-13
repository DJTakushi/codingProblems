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

class xNode:
    nodeList=list()

    def __init__(self,val,prev=0,next=0):
        self.val=val
        if(len(xNode.nodeList)==0):
            xNode.headNode=self
        xNode.nodeList.append(self)
        self.pointer = len(xNode.nodeList)-1 #pointer is the idx in the list
        # self.setboth(prev,next)
    def getPointer(self):
        return self.pointer
    def setboth(self,prev,next):
        self.both=prev^next
    def getOther(self,addr):
        return addr^self.both
    def dereferencePointer(x):
        return xNode.nodeList[x]
    def add(element):
        xNode(element)
    def get(index):
        thisNode=xNode.headNode
        prevAdd=0#firs previous pointer is 0
        while(index):
            tempAdd=thisNode.getPointer()
            thisNode=thisNode.getOther(prevAdd)
            prevAdd=tempAdd
        return


import unittest
class xNodeTest(unittest.TestCase):
    def testXnode(self):
        node0=xNode(556)
        node1=xNode(762)
        node2=xNode(1270)
        self.assertEqual(0,node0.getPointer())
        self.assertEqual(556,node0.val)
        self.assertEqual(1,node1.getPointer())
        self.assertEqual(762,node1.val)
        self.assertEqual(2,node2.getPointer())
        self.assertEqual(1270,node2.val)
        node1.setboth(node0.getPointer(),node2.getPointer())
        self.assertEqual(node0.getPointer(),node1.getOther(node2.getPointer()))
        self.assertEqual(node2.getPointer(),node1.getOther(node0.getPointer()))


if __name__=="__main__":
    unittest.main()
