import os,sys,unittest,importlib,testHelper
class myTest(unittest.TestCase):
    def testThis(self):
        import az05,azBinTree
        head=azBinTree.node(100)
        node2=head.createLeft(50)
        node2.createLeft(25)
        node2.createRight(75)
        node2=head.createRight(200)
        node2.createRight(350)
        received=az05.level_order_traversalR(head)
        expected="100 50 200 25 75 350 "#example online ends with an excessive space at the end.  C'MON, MAN!!!
        self.assertEqual(expected,received)
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
