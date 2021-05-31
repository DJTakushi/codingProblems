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
