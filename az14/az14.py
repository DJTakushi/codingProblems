def find_low_index(arr, key):
    poI=find_pointOfImpact(arr,key)
    if poI==-1:
        return poI
    while poI != 0:
        if arr[poI-1] == key:
            poI-=1
        else:
            return poI
    return poI

def find_high_index(arr, key):
    poI=find_pointOfImpact(arr,key)
    if poI==-1:
        return poI
    while poI != (len(arr)-1):
        if arr[poI+1] == key:
            poI+=1
        else:
            return poI
    return poI

def find_pointOfImpact(arr,key):
    arrSize=len(arr)
    if key < arr[0]:
        return -1
    if key > arr[arrSize-1]:
        return -1
    cIdx=arrSize-1
    divPow=2
    prevIdx=0
    while arr[cIdx] != key:
        #print("...cIdx="+str(cIdx))
        step=arrSize//divPow
        if step==0:
            step=1
        #print("..step="+str(step))
        if arr[cIdx] > key:
            cIdx-=step
        else:
            cIdx+=step
        if cIdx==prevIdx:
            break
        else:
            prevIdx=cIdx
        divPow*=2
    return cIdx
