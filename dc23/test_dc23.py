import os,sys,unittest,importlib
import dc23
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        board=[['f', 'f', 'f', 'f'],['t', 't', 'f', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']]
        self.assertEqual(7,dc23.solve(board,(3,0),(0,0)))

        #fail due to no path available
        board=[['f', 'f', 'f', 'f'],['t', 't', 't', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']]
        self.assertEqual(-1,dc23.solve(board,(3,0),(0,0)))

        # " [[f, f, f, f],\n" zig-zag all the way
        # "  [t, t, t, f],\n"
        # "  [f, f, f, f],\n"
        # "  [f, t, t, t],\n"
        # "  [f, f, f, f]]\n"
        board=[['f', 'f', 'f', 'f'],['t', 't', 't', 'f'],['f', 'f', 'f', 'f'],['f', 't', 't', 't'],['f', 'f', 'f', 'f']]
        self.assertEqual(13,dc23.solve(board,(4,3),(0,0)))
        board=[['f', 'f', 'f', 'f'],['t', 't', 't', 'f'],['f', 'f', 'f', 'f'],['f', 't', 't', 't'],['f', 'f', 'f', 'f']]
        self.assertEqual(10,dc23.solve(board,(4,0),(0,0)))
if __name__=="__main__":
    unittest.main()
