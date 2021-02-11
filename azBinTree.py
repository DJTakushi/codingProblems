class node:
    def __init__(self,data,previous=None):
        self.data=data
        self.left=None
        self.right=None
    def createLeft(self,data):
        newNode=node(data)
        self.left=newNode
        return newNode
    def createRight(self,data):
        newNode=node(data)
        self.right=newNode
        return newNode
    def printLR(self):
        if self.left != None:
            self.left.printLR()
        print(self.data)
        if self.right != None:
            self.right.printLR()

class deque:
    def __init__(self):
        self.list=[]
    def append(self,node):
        self.list.append(node)
    def popleft(self):
        if not self.list:
            return
        return self.list.pop(0)

def testNode():
    head=node(100)
    node2=head.createLeft(50)
    node2.createLeft(25)
    node2.createRight(75)
    node2=head.createRight(200)
    node2.createRight(350)
    head.printLR()
#testNode()
