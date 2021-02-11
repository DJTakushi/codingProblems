from azBinTree import  *
#https://www.educative.io/blog/crack-amazon-coding-interview-questions
def is_bst(root):
  #TODO: Write - Your - Code
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
def test_is_bst():
    head=node(100)
    node2=head.createLeft(50)
    node2.createLeft(25)
    node2.createRight(75)
    node2=head.createRight(200)
    node2.createLeft(125)
    node2.createRight(350)
    received=is_bst(head)
    expected=True
    if received==expected:
        print("Pass")
    else:
        print("FAIL!!!  Expected "+str(expected))
    node2.createLeft(90)
    received=is_bst(head)
    expected=False
    if received==expected:
        print("Pass")
    else:
        print("FAIL!!!  Expected "+str(expected))

test_is_bst()
