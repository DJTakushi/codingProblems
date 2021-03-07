#https://www.dailycodingproblem.com/
from takTest import *
def printProblem():
    print("There's a staircase with N steps, and you can climb 1 or 2 steps\n"
            "at a time. Given N, write a function that returns the number of\n"
            "unique ways you can climb the staircase.\n"
            "The order of the steps matters.\n"
            "For example, if N is 4, then there are 5 unique ways:\n"
            "   1, 1, 1, 1\n"
            "   2, 1, 1\n"
            "   1, 2, 1\n"
            "   1, 1, 2\n"
            "   2, 2\n"
            "What if, instead of being able to climb 1 or 2 steps at a time,\n"
            "you could climb any number from a set of positive integers X?\n"
            "For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps\n"
            "at a time. Generalize your function to take in X.")
# look at cases:
# N = 1: [1] (1)
# N = 2: [1, 1], [2] (2)
# N = 3: [1, 2], [1, 1, 1], [2, 1] (3)
# N = 4: [1, 1, 2], [2, 2], [1, 2, 1], [1, 1, 1, 1], [2, 1, 1] (5)
# Note that the trend is f(n)=f(n-1)+f(n-2).
# This makes sense since in n-1 and n-2, the n-x evalutaion represents the combo
#  that will simply have x added to them at the end.  This allows us to evaulate
#  a funtion at a lower order, which will be eaier.
def staircaseW(data):
    return(staircaseFinal(data.n,data.X))
def staircfacasebase(n):
    #indexes are 1 & 2
    if n <= 1:
        return 1
    return staircasebase(n - 1) + staircasebase(n - 2)
def staircaseGeneralized(n, X):#generalized,
    #but slow since it has to be computed several times
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircaseGeneralized(n - x, X) for x in X)#recursive call for each index in X is slow!!
def staircasefinal(n, X): #ripped off online end solution.  I'm trash.
    cache = [0 for _ in range(n + 1)] #blank cache
    cache[0] = 1#1 in Fibonacci sequence
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]
class fdata:
    def __init__(self,n,X):
        self.n=n
        self.X=X
    def print(self):
        print("  n = "+str(self.n))
        print("  X = "+str(self.X))
def getTestVector():
    testVector=list()
    testVector.append(testCase(fdata(1,[2,1]),1))
    testVector.append(testCase(fdata(2,[2,1]),2))
    testVector.append(testCase(fdata(3,[2,1]),3))
    testVector.append(testCase(fdata(4,[2,1]),5))
    return testVector
test(staircaseW,getTestVector())
