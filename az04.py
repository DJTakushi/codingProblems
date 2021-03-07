from azLinkedList import  *
#https://www.educative.io/blog/crack-amazon-coding-interview-questions

def deep_copy_arbitrary_pointer(head):
    if head==None:
        return
    nodeDict={} # key = old node, value = new node
    currentNode=head
    previousNewNode=None
    while(currentNode!=None):
        nodeCopy=LinkedListNode(currentNode.data)
        nodeDict[currentNode]=nodeCopy
        nodeCopy.arbitrary=currentNode.arbitrary;#save old node; will be updated later
        if previousNewNode!=None:
            previousNewNode.next=nodeCopy
        previousNewNode=nodeCopy
        currentNode=currentNode.next

    newHead=nodeDict[head]
    currentNode=newHead
    while(currentNode!=None):
        if currentNode.arbitrary:
            currentNode.arbitrary=nodeDict[currentNode.arbitrary] #look up stored old value and update with dictionary value for new node
        currentNode=currentNode.next
    return newHead

def test_deep_copy_arbitrary_pointer():
    myTestNode=LinkedListNode([4,7,8,9,10,15,16,19],"list")
    myTestNode.applyArbitrary([7,6,4,4,3,2,1,0])
    myDeepCopy=deep_copy_arbitrary_pointer(myTestNode)

    result=myTestNode.checkMatches(myDeepCopy)
    if result:
        print("Pass")
    else:
        print("FAILURE!!!")
test_deep_copy_arbitrary_pointer()
