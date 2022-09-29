# https://leetcode.com/problems/middle-of-the-linked-list/
# Given the head of a singly linked list, return the middle node of the linked list.
#
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def createList(inList):
    previous=None
    head = None
    for i in inList:
        ln = ListNode(i)
        if head == None:
            head = ln
        if previous:
            previous.next = ln
        previous = ln
    return head
def getListOfValues(head):
    o = []
    o.append(head.val)
    if head.next:
        o= o + getListOfValues(head.next)
    return o

class Solution:
    def middleNode(self, head):
        o = head
        l = self.getLen(head)
        # print("l="+str(l))

        # casting to int floors it down
        # int(5/2) = 2, the correct index
        # int(6/2) = 3, the correct6 index
        target = int(l/2)
        # print("target="+str(target))

        # print("o.val="+str(o.val))
        for i in range(target):
            o = o.next
            # print("o.val="+str(o.val))

        return o
    def getLen(self,head):
        o = 0
        while(head):
            o+=1
            head = head.next
        return o


if __name__=="__main__":
    sol = Solution()
    l = ["1","2","3","4","5"]
    h = createList(l)
    o = sol.middleNode(h)
    o = getListOfValues(o)
    print(o)

    assert 3 == len(o)
    assert "3"==o[0]
    assert "4"==o[1]
    assert "5"==o[2]

    l = ["1","2","3","4","5","6"]
    h = createList(l)
    o = sol.middleNode(h)
    o = getListOfValues(o)
    assert 3 == len(o)
    assert "4"==o[0]
    assert "5"==o[1]
    assert "6"==o[2]
