import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import az04
        import azLinkedList
        myTestNode=azLinkedList.LinkedListNode([4,7,8,9,10,15,16,19],"list")
        myTestNode.applyArbitrary([7,6,4,4,3,2,1,0])
        myDeepCopy=az04.deep_copy_arbitrary_pointer(myTestNode)
        self.assertEqual(True,myTestNode.checkMatches(myDeepCopy))
if __name__=="__main__":
    unittest.main()
