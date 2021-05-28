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
