import os,sys,unittest,importlib,testHelper
import dc03
class myTest(unittest.TestCase):
    def test_this(self):
        myNode = dc03.Node('root', dc03.Node('left', dc03.Node('left.left')), dc03.Node('right'))
        self.assertEqual("left.left left root right",dc03.serialize(myNode))
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.left.val,'left.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.val,'left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.val,'right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).val,'root')

        myNode = dc03.Node('root', dc03.Node('left', dc03.Node('left.left'), dc03.Node('left.right')), dc03.Node('right'))
        self.assertEqual("left.left left left.right root right",dc03.serialize(myNode))
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.left.val,'left.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.right.val,'left.right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.val,'left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.val,'right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).val,'root')

        myNode = dc03.Node('root', dc03.Node('left', dc03.Node('left.left'), dc03.Node('left.right')), dc03.Node('right',dc03.Node('right.left')))
        self.assertEqual("left.left left left.right root right.left right",dc03.serialize(myNode))
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.left.val,'left.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.right.val,'left.right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.val,'left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.val,'right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.left.val,'right.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).val,'root')

        myNode = dc03.Node('root', dc03.Node('left', dc03.Node('left.left'), dc03.Node('left.right')), dc03.Node('right',dc03.Node('right.left'),dc03.Node('right.right')))
        self.assertEqual("left.left left left.right root right.left right right.right",dc03.serialize(myNode))
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.left.val,'left.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.right.val,'left.right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.val,'left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.val,'right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.left.val,'right.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.right.val,'right.right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).val,'root')

        myNode = dc03.Node('root', dc03.Node('left', dc03.Node('left.left')), dc03.Node('right',dc03.Node('right.left'),dc03.Node('right.right')))
        self.assertEqual("left.left left root right.left right right.right",dc03.serialize(myNode))
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.left.val,'left.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.val,'left')
        #all below will fail - tree is built top->down and left->right.  Cannot have skipped indexes.
        # self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.val,'right')
        # self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.left.val,'right.left')
        # self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.right.val,'right.right')
        # self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).val,'root')

        myNode = dc03.Node('root', dc03.Node('left', dc03.Node('left.left',dc03.Node('left.left.left')), dc03.Node('left.right')), dc03.Node('right',dc03.Node('right.left'),dc03.Node('right.right')))
        self.assertEqual("left.left.left left.left left left.right root right.left right right.right",dc03.serialize(myNode))
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.left.val,'left.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.left.left.val,'left.left.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.right.val,'left.right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).left.val,'left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.val,'right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.left.val,'right.left')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).right.right.val,'right.right')
        self.assertEqual(dc03.deserialize(dc03.serialize(myNode)).val,'root')

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
