def printProblem():
    print("Daily Coding Problem: Problem #23 [Easy]\n"
            "This problem was asked by Google.\n"
            "You are given an M by N matrix consisting of booleans that\n"
            "represents a board. Each True boolean represents a wall. Each\n"
            "False boolean represents a tile you can walk on.\n"
            "Given this matrix, a start coordinate, and an end coordinate,\n"
            "return the minimum number of steps required to reach the end\n"
            "coordinate from the start. If there is no possible path, then\n"
            "return null. You can move up, left, down, and right. You cannot\n"
            "move through walls. You cannot wrap around the edges of the board.\n"
            "For example, given the following board:\n"
            " [[f, f, f, f],\n"
            "  [t, t, f, t],\n"
            "  [f, f, f, f],\n"
            "  [f, f, f, f]]\n"
            "and start = (3, 0) (bottom left) and end = (0, 0) (top left),\n"
            "the minimum number of steps required to reach the end is 7, since\n"
            "we would need to go through (1, 2) because there is a wall\n"
            "everywhere else on the second row.")

def getC(point,dir):
    if dir=="n":
        return (point[0]-1,point[1])
    if dir=="e":
        return (point[0],point[1]+1)
    if dir=="s":
        return (point[0]+1,point[1])
    if dir=="w":
        return (point[0],point[1]-1)

def solve(b,start,end,pPath=None):
    up=(start[0]-1,start)


import unittest
class myTest(unittest.TestCase):
    def testThis(self):
        board=[['f', 'f', 'f', 'f'],['t', 't', 'f', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']]
        self.assertEqual(7,solve(board,(3,0),(0,0)))
