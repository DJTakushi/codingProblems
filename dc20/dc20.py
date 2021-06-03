class node():
    def __init__(self,val, next=None):
        self.val=val
        self.n=next

def findIntersect(A,B):
    aValSet=set() #not actually constant space.  Could use a better hash or something
    while A:
        aValSet.add(A.val)
        A=A.n
    while B:
        if B.val in aValSet:
            return B
        B=B.n
    return -1
