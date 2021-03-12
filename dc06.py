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
    count = 0
    nodeList=list()
    def __init__(self,val,prev=0,next=0):
        self.val=val
        self.pointer = count
        count+=1
        self.setboth(prev,next)
    def setboth(prev,next):
        self.both=xor(prev,next)
    def getOther(addr)
        return
