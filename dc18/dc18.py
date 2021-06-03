def maxValOSubArray(ar, k):
    out=list()
    for i in range(len(ar)+1-k):
        out.append(max(ar[i:i+k])) #this operates at O(k) though
    return out

def maxValOSubArrayFAST(ar, k):
    # preserve the current max
    # replace it if
    #     the next entered one is the new max
    #     OR it has expired
    #         Will then have to recompute with O(k) though
    return -1
