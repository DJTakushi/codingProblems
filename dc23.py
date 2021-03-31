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
    #print("start = ("+str(start[0])+","+str(start[1])+"), end = ("+str(end[0])+","+str(end[1])+")")
    if not pPath:
        pPath = set()
    if start == end:
        #print(" got it!  Set list = "+str(len(pPath)))
        return len(pPath)#hit target - return path length
    else:
        if start in pPath: #overlapping path is stupid.  ABORT!
            return -1
        if start[0] >= len(b) or start[0] < 0:#y out of range
            return -1
        if start[1] >= len(b[start[0]]) or start[1] < 0:#x out of range
            return -1
        if b[start[0]][start[1]]=='t': #we're in a wall.  ABORT!
            return -1
        pPath.add(start)
        rl=list()
        rl.append(solve(b,getC(start,"n"),end,pPath.copy()))
        rl.append(solve(b,getC(start,"s"),end,pPath.copy()))
        rl.append(solve(b,getC(start,"e"),end,pPath.copy()))
        rl.append(solve(b,getC(start,"w"),end,pPath.copy()))
        if len(rl):
            min=max(rl)
            for i in rl:
                if i < min and i != -1:
                    min = i
            return min
        else:
            return -1

import unittest
class myTest(unittest.TestCase):
    def testThis(self):
        board=[['f', 'f', 'f', 'f'],['t', 't', 'f', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']]
        self.assertEqual(7,solve(board,(3,0),(0,0)))

        #fail due to no path available
        board=[['f', 'f', 'f', 'f'],['t', 't', 't', 't'],['f', 'f', 'f', 'f'],['f', 'f', 'f', 'f']]
        self.assertEqual(-1,solve(board,(3,0),(0,0)))

        # " [[f, f, f, f],\n" zig-zag all the way
        # "  [t, t, t, f],\n"
        # "  [f, f, f, f],\n"
        # "  [f, t, t, t],\n"
        # "  [f, f, f, f]]\n"
        board=[['f', 'f', 'f', 'f'],['t', 't', 't', 'f'],['f', 'f', 'f', 'f'],['f', 't', 't', 't'],['f', 'f', 'f', 'f']]
        self.assertEqual(13,solve(board,(4,3),(0,0)))
        board=[['f', 'f', 'f', 'f'],['t', 't', 't', 'f'],['f', 'f', 'f', 'f'],['f', 't', 't', 't'],['f', 'f', 'f', 'f']]
        self.assertEqual(10,solve(board,(4,0),(0,0)))

if __name__=="__main__":
    unittest.main()
