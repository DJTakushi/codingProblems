# https://leetcode.com/problems/find-k-closest-elements/
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
import json
def tprint(s):
    if False:
        print(s)
class closestList:
    def __init__(self, k, x):
        self.k = k
        self.x = x
        self.list = []
    def addToEnd(self,i,q):
        # print("addToEnd("+str(i)+","+str(q)+")")
        while q > 0:
            if len(self.list) < self.k:
                self.list.append(i)
            else:
                break
            q -=1
        # print("  returning "+str(q)+" with list: "+str(self.list))
        return q
def closerThan(a, b, x):
    o = False
    if a != None and b == None:
        o = True
    elif a == None and b != None:
        o = False
    else:
        aC = abs(a-x)
        bC = abs(b-x)
        if aC < bC or (aC==bC and a<b):
            tprint(str(a)+" closer to "+str(x)+" than "+str(b) + " ["+str(aC)+" vs "+str(bC)+"]")
            o = True
    return o
class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        o = [ ]
        cL = closestList(k,x)
        iTgt = self.findLastImpactIndex(arr, x)
        idxL = iTgt
        idxR = iTgt+1
        l = arr[idxL]
        r = 0
        if idxR < len(arr):
            r = arr[idxR]
        else:
            r = None
        while len(cL.list) < k:
            quantity = 1
            if closerThan(l, r, x):
                idx_X_next = idxL-1
                while idx_X_next >= 0:
                    if l==arr[idx_X_next]:
                        quantity+=1
                        idx_X_next-=1
                        if idx_X_next < 0:
                            break
                    else:
                        break
                qRemaining = cL.addToEnd(l,quantity)
                if qRemaining > 0:
                    break
                else:
                    if 0 <= idx_X_next:
                        idxL = idx_X_next
                        l = arr[idxL]
                    else:
                        l = None
            else:
                idx_X_next = idxR+1
                while idx_X_next < len(arr):
                    if r==arr[idx_X_next]:
                        quantity+=1
                        idx_X_next+=1
                        if idx_X_next < len(arr):
                            break
                    else:
                        break
                qRemaining = cL.addToEnd(r,quantity)
                if qRemaining > 0:
                    break
                else:
                    if idx_X_next < len(arr):
                        idxR = idx_X_next
                        r = arr[idxR]
                    else:
                        r = None
        o = cL.list
        o.sort()
        return o

    def findLastImpactIndex(self, a, x):
        ### returns last index of a precise match.
        ### If a precise match is not found, takes the closest (I.E.: the lower index)
        o = 0
        while o+1 < len(a):
            current = a[o]
            target = a[o+1]
            if closerThan(target, current,x) or current == target:
                o+=1
            else:
                print("a[o+1]("+str(a[o+1])+") not closer than a[o]("+str(a[o])+") - returning o="+str(o))
                break
        return o

if __name__=="__main__":
    data = {}
    with open('testCases.json') as f:
       data = json.load(f)
    sol = Solution()
    print("CASE 0:")
    o = sol.findClosestElements([1,2,3,4,5],4,3)
    print(o)
    assert 4 == len(o)
    assert 1 == o[0]
    assert 2 == o[1]
    assert 3 == o[2]
    assert 4 == o[3]

    print("CASE 1:")
    o = sol.findClosestElements([1,2,3,4,5],4,-1)
    print(o)
    assert 4 == len(o)
    assert 1 == o[0]
    assert 2 == o[1]
    assert 3 == o[2]
    assert 4 == o[3]

    print("CASE 2:")
    o = sol.findClosestElements([0,0,0,0,1,1,1,1,2,3,4,5],4,-1)
    print(o)
    assert 4 == len(o)
    assert 0 == o[0]
    assert 0 == o[1]
    assert 0 == o[2]
    assert 0 == o[3]

    print("CASE 3:")
    o = sol.findClosestElements([1,1,1,10,10,10],1,9)
    print(o)
    assert 1 == len(o)
    assert 10 == o[0]

    print("CASE 4:")
    o = sol.findClosestElements([0,0,0,1,3,5,6,7,8,8],2,2)
    print(o)
    assert 2 == len(o)
    assert 1 == o[0]
    assert 3 == o[1]

    print("CASE 5:")
    # print("TESTING PROBLEM")
    dumbArray = data['testCase5']['arr']
    o = sol.findClosestElements(dumbArray,3560,4319)

    expected = data['testCase5']['expected']
    assert len(expected) == len(o)
    print(" checking "+str(len(expected))+" elements...")
    for i in range(len(expected)):
        assert expected[i] == o[i]

    print("CASE 6:")
    dumbArray = data['testCase6']['arr']
    o = sol.findClosestElements(dumbArray,6399,-28)
    # print(o)
    assert 6399 == len(o)

    print("CASE 7:")
    o = sol.findClosestElements([-2,-1,1,2,3,4,5],7,3)
    assert 7 == len(o)
    assert -2 == o[0]
    assert -1 == o[1]
    assert 1  == o[2]
    assert 2  == o[3]
    assert 3  == o[4]
    assert 4  == o[5]
    assert 5  == o[6]

    print("done.")
