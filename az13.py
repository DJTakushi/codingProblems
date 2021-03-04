#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def printPrompt():
    print("13. Clone a Directed Graph\n"
        "  Given the root node of a directed graph, clone this graph by \n"
        "  creating its deep copy so that the cloned graph has the same\n"
        "  vertices and edges as the original graph.")
class Node:
  def __init__(self, d):
    self.data = d
    self.neighbors = []
def clone(root):
    #nodeSet=set()#set of nodes that have been visited yet
    nodeDict=dict()#key = old node, value=new nodes
    newRoot=cloneNode(root,nodeDict)
    return newRoot    # return root
def cloneNode(subject,nodeDict):
    if subject in nodeDict:
        return nodeDict[subject]
    #clone to new node with same data
    newNode=Node(subject.data)

    #add to ditionary
    nodeDict[subject]=newNode

    #populate new reference with new ones
    for neighbor in subject.neighbors:
        newNode.neighbors.append(cloneNode(neighbor,nodeDict))
    return newNode
def nodeNetworkDict(node,networkDict):
    if node.data in networkDict:
        return
    else:
        neighborIdList=list()
        for n in node.neighbors:
            neighborIdList.append(n.data)
        networkDict[node.data]=neighborIdList
    for n in node.neighbors:
        nodeNetworkDict(n,networkDict)
def compareNodeNetworks(node1,node2):
    dict1=dict()
    dict2=dict()
    nodeNetworkDict(node1,dict1)
    nodeNetworkDict(node2,dict2)
    dict1Len=len(dict1)
    dict2Len=len(dict2)
    if dict1Len != dict2Len:
        print("FAIL!!!  dict1 len = "+str(dict1Len)+" but dict2 len = "+str(dict2Len))
        return False
    else:
        for key in dict1:
            if key not in dict2:
                print("FAIL!!! key "+str(key)+" not in dict2!")
                return False
            else:
                if dict1[key]!=dict2[key]:
                    print("FAIL!!! dict1["+str(key)+"]="+str(dict1[key])+" but dict2["+str(key)+"]="+str(dict2[key]))
                    return False
    return True
def test():
    n0=Node(0)
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n0.neighbors=[n2,n3,n4]
    n1.neighbors=[n2]
    n2.neighbors=[n0]
    n3.neighbors=[n2]
    n4.neighbors=[n0,n1,n3]
    if(compareNodeNetworks(n0,clone(n0))):
        print("Pass.")

    n0=Node(0)
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n6=Node(6)
    n0.neighbors=[n4,n5,n2,n1,n6,n3]
    n1.neighbors=[n5,n2,n0,n4,n6]
    n2.neighbors=[n5,n4,n1,n0,n3]
    n3.neighbors=[n4,n2,n5,n6,n0]
    n4.neighbors=[n0,n2,n3,n5,n6,n1]
    n5.neighbors=[n1,n2,n0,n4,n3]
    n6.neighbors=[n0,n4,n3,n1]
    if(compareNodeNetworks(n0,clone(n0))):
        print("Pass.")
test()
