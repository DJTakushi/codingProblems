def binary_search_rotated(arr, key):
    s=0#start
    e=len(arr)-1
    m=((e-s)//2)+s
    while(arr[m] != key):
        #print("s,m,e = "+str(s)+","+str(m)+","+str(e))
        if s==e:
            return -1
        if key < arr[m]:
            if arr[s] < arr[m] and key < arr[s]:
                s=m+1
            else:
                e=m-1
        else:
            if arr[m] < arr[e] and key > arr[e]:
                e=m-1
            else:
                s=m+1
        m=((e-s)//2)+s
    return m
