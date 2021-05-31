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
