import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import az06,azBinTree
        head=azBinTree.node(100)
        node2=head.createLeft(50)
        node2.createLeft(25)
        node2.createRight(75)
        node2=head.createRight(200)
        node2.createLeft(125)
        node2.createRight(350)
        received=az06.is_bst(head)
        expected=True
        self.assertEqual(expected,received)

        node2.createLeft(90)
        received=az06.is_bst(head)
        expected=False
        self.assertEqual(expected,received)
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
