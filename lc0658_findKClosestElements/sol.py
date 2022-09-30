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
    def add(self, i,q):
        o = False
        insertIdx = len(self.list)
        # try:
        #     while insertIdx >= 0 and closerThan(i,self.list[insertIdx], self.x):
        #         insertIdx-=1
        # except:
        #     pass

        if insertIdx!=0:
            # g = True
            while True:
                if insertIdx > 0:
                    incumbent = self.list[insertIdx-1]
                    if closerThan(i,incumbent, self.x):
                        insertIdx-=1
                    else:
                        break
                else:
                    break

        tprint("i: "+str(i)+", insertIdx="+str(insertIdx))
        while insertIdx < self.k and q > 0:
            self.list.insert(insertIdx,i)
            q-=1
            tprint("inserting i:"+str(i)+"; list = "+str(self.list))
        o = q==0
        while len(self.list)>self.k:
            self.list.pop()
        return o

def closerThan(a, b, x):
    o = False
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
        NAIVE = False
        if NAIVE:
            for i in arr:
                cL.add(i,1)
        else:
            iTgt=self.findLastImpactIndex(arr,x)
            print("iTgt:"+str(iTgt))
            OldStyle=False
            if OldStyle:
                i = iTgt
                good=True
                print("counting down at i="+str(i))
                while good:
                    try:
                        good = cL.add(arr[i],1)
                        i-=1
                    except:
                        print("broke!!! i="+str(i))
                        good = False
                    good = good and i >= 0
                good = True
                i = iTgt+1 # don't add arr[iTgt] twice!
                print("counting up at i="+str(i))
                while good:
                    try:
                        good = cL.add(arr[i],1)
                        i+=1
                    except:
                        good = False
                    # good = good and i < len(arr)
            else:
                idxL = iTgt
                idxR = iTgt+1
                continueLeft = idxL >= 0
                continueRight = idxR < len(arr)
                while continueLeft or continueRight:
                    if continueLeft:
                        # print("  idxL:"+str(idxL))
                        idxL2 = idxL
                        quantity = 0 # counter for quanitty of this element
                        good = True
                        while good:
                            quantity+=1
                            good = False
                            idxL2-=1
                            if idxL2 >=0:
                                good = arr[idxL2] == arr[idxL]
                        continueLeft = cL.add(arr[idxL], quantity)
                        idxL = idxL2
                        continueLeft = idxL >=0
                    if continueRight:
                        # print("  idxR:"+str(idxR))
                        idxR2 = idxR
                        quantity = 0
                        good = True
                        while good:
                            quantity+=1
                            good = False
                            idxR2+=1
                            if idxR2 < len(arr):
                                good = arr[idxR2] == arr[idxR]
                        continueRight = cL.add(arr[idxR],quantity)
                        idxR = idxR2
                        continueRight = idxR < len(arr)
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
    print(o)
    assert 6399 == len(o)
