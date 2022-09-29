#https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        # print("created ListNode with value "+ str(self.val))
    def getListString(self):
        s = str(self.val)
        if self.next:
            s+=" " + self.next.getListString()
        return s
    def printList(self):
        print(self.getListString())
class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    def isPalindrome(self, head) -> bool:
        out = True
        head.printList()
        idx2 = self.getSecondHalfIdx(head)
        print("idx2 = "+str(idx2))

        # head = self.reverseAtHead(head)
        secondHead = self.getNode(head, idx2)
        # secondHead.printList()
        reverseHead = self.reverseAtHead(secondHead)
        reverseHead.printList()

        nLeft = head
        nRight = reverseHead
        while(nLeft and nRight):
            if nLeft.val != nRight.val:
                out = False
                print(str(nLeft.val)+" != "+str(nRight.val))
            nLeft = nLeft.next
            nRight = nRight.next

        return out
    def getTotalLength(self,head):
        o = 0
        current = head
        while current:
            o+=1
            current = current.next
        return o
    def getSecondHalfIdx(self,head):
        length = self.getTotalLength(head)
        return int(length/2)+int(length%2)
    def getNode(self,head,i):
        while(head != None and i > 0):
            head = head.next
            i-=1
        return head
    def reverseAtHead(self,head):
        current = head
        previous = None
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

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

if __name__=="__main__":
    head = createList(["1","2","2","1"])
    # head = createList(["1","2","3","4"])
    s = Solution()
    o = "null"
    o = s.isPalindrome(head)
    print((o))
