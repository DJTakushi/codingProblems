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
