#dailyCoding problem#3
def printProblem():
    print("Given the root to a binary tree, implement\n"
            "serialize(root), which serializes the tree into a string, and\n"
            "deserialize(s), which deserializes the string back into the tree.")
class Node:#provided
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    return getBinaryNode(node)[0:-1]

delim=" "
def getBinaryNode(node):
    output=""
    if node.left:
        output+=(getBinaryNode(node.left))
    output+=(node.val+delim)
    if node.right:
        output+=(getBinaryNode(node.right))
    return output

def deserialize(s):
    return node



import unittest
class UnitTest(unittest.TestCase):
    def test_case(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        # assert deserialize(serialize(node)).left.left.val == 'left.left'
        self.assertEqual("left.left left root right",serialize(node))
if __name__=='__main__':
    unittest.main()
