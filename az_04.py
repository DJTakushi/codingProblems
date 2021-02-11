from azLinkedList import  *


#testLinkedList=linkedList([4,7,8,9,10,15,16,19])
#testHead=testLinkedList.getHead()

def deep_copy_arbitrary_pointer(head):
    nodeDict={} # key = old node, value = new node
    currentNode=head
    previousNewNode=None
    while(currentNode!=None):
        nodeCopy=LinkedListNode([currentNode.data])
        nodeDict[currentNode]=nodeCopy
        nodeCopy.arbitrary=currentNode.arbitrary#save old node; will be updated later
        if previousNewNode!=None:
            previousNewNode.next=nodeCopy
        previousNewNode=nodeCopy
        currentNode=currentNode.next

    newHead=nodeDict[head]
    currentNode=newHead
    while(currentNode!=None):
        currentNode.arbitrary=nodeDict[currentNode.arbitrary]#look up stored old value and update with dictionary value for new node
        currentNode=currentNode.next
    return newHead

myTestNode=LinkedListNode([4,7,8,9,10,15,16,19])
myTestNode.applyArbitrary([7,6,4,4,3,2,1,0])
myDeepCopy=deep_copy_arbitrary_pointer(myTestNode)
print(myTestNode.checkMatches(myDeepCopy))
print(myTestNode.exportList())
print(myDeepCopy.exportList())
