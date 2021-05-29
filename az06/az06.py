from azBinTree import  *
def is_bst(root):
  return recursiveFunction(root,0,900)

def recursiveFunction(node, min, max):
    if node.data > max:
        return False
    if node.data < min:
        return False
    if node.left:
        if not recursiveFunction(node.left,min,node.data):
            return False
    if node.right:
        if not recursiveFunction(node.right,node.data,max):
            return False
    return True
