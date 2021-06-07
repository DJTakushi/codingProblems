import os,sys,unittest,importlib
import dc21
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        cmm=dc21.classRoomManager([(30,75),(0,50),(0,150)])
        self.assertEqual(2,cmm.getClassRoomQuanity())
if __name__=="__main__":
    unittest.main()
