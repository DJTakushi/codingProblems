# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
#
# A row i is weaker than a row j if one of the following is true:
#
# The number of soldiers in row i is less than the number of soldiers in row j.
# Both rows have the same number of soldiers and i < j.
# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
class rr:
    def __init__(self, idx, strength=0):
        self.idx = idx
        self.strength = strength
class rrHolder:
    def __init__(self, k):
        self.l = [] # list of rr objects
        self.k = k
    def add(self, rr_i):
        idx=0
        # print("rrHolder.add: rr_i.idx:"+str(rr_i.idx)+", rr_i.strength:"+str(rr_i.strength))
        try:
            # increment idx if rr_i is stronger than idx in list
            while rr_i.strength >= self.l[idx].strength:
                idx+=1
        except: # catch breaks when idx out of range
            pass
        if idx < self.k:
            # print(" inserting at idx:"+str(idx))
            self.l.insert(idx,rr_i)
        while len(self.l)>self.k:
            self.l.pop()
    def getResults(self):
        o = []
        for i in self.l:
            o.append(i.idx)
        # print("rrHolder.getResults() returns "+str(o))
        return o


def getRowStrength(l):
    o = 0
    for i in range(len(l)):
        if l[i]==1:
            o+=1
        else:
            break
    return o

class Solution:
    def kWeakestRows(self, mat, k):
        o = []
        rrh=rrHolder(k)
        for i in range(len(mat)):
            row_t = mat[i]
            rr_t = rr(i, getRowStrength(row_t))
            rrh.add(rr_t)
        o = rrh.getResults()
        return o


if __name__=="__main__":
    sol = Solution()
    mat = []
    mat.append([1,1,0,0,0])
    mat.append([1,1,1,1,0])
    mat.append([1,0,0,0,0])
    mat.append([1,1,0,0,0])
    mat.append([1,1,1,1,1])
    k = 3
    o = sol.kWeakestRows(mat,k)

    assert 3 == len(o)
    assert 2 == o[0]
    assert 0 == o[1]
    assert 3 == o[2]


    mat = []
    mat.append([1,0,0,0])
    mat.append([1,1,1,1])
    mat.append([1,0,0,0])
    mat.append([1,0,0,0])
    k = 2
    o = sol.kWeakestRows(mat,k)

    assert 2 == len(o)
    assert 0 == o[0]
    assert 2 == o[1]
