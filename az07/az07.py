def can_segment_string(s, dictionary):
    strLen=len(s)
    hashSet=set()
    for idx in range(strLen):
        markToContinue=False
        a=s[0:idx]
        b=s[idx:strLen]
        if a not in dictionary:
            hashSet.add(a)
            markToContinue=True
        if b not in dictionary:
            hashSet.add(b)
            markToContinue=True
        if not markToContinue:
            return True
    return False
