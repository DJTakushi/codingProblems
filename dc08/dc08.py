

def univalCount(headNode, val=None):
    if not val:
        val=0
    count = 0
    headPotential=True
    if not headNode.left and not headNode.right:#bottom node
        return 1

    if headNode.left:
        leftResult=univalCount(headNode.left,val+1)
        count+=abs(leftResult)
        if headNode.val != headNode.left.val or leftResult < 0:
            headPotential=False
    if headNode.right:
        rightResult=univalCount(headNode.right,val+1)
        count+=abs(rightResult)
        if headNode.val != headNode.right.val or rightResult < 0:
            headPotential=False
    if (headNode.left or headNode.right) and headPotential:
        count+=1
    if not headPotential and val > 0:
        count*=-1
    return count


class node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left=left
        self.right=right
