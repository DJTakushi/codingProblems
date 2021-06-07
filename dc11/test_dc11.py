import os,sys,unittest,importlib
import dc11
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        headNode=dc11.node("dog")
        headNode.add("deer")
        headNode.add("deal")
        headNode.add("cat")
        self.assertEqual(["dog","deer","deal","cat"],headNode.getAll())
        self.assertEqual(["dog"],headNode.getAll("do"))
        self.assertEqual(["dog","deer","deal"],headNode.getAll("d"))
        self.assertEqual(["deer","deal"],headNode.getAll("de"))
        self.assertEqual(["cat"],headNode.getAll("c"))
if __name__=="__main__":
    unittest.main()
