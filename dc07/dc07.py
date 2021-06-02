alphaSet=set()
for i in range(0,27):
    alphaSet.add(str(i))

def decode(msg,decodeSet=alphaSet):
    if len(msg)==0:
        return 1
    oneLetterVal=msg[0]
    sum=0
    if oneLetterVal in decodeSet:
        if len(msg)==1:
            sum+=1
        else:
            sum+=decode(msg[1:])#recursively call with remainder
    if len(msg)>=2:
        twoLetterVal=msg[:2]
        if twoLetterVal in decodeSet:
            if len(msg)==2:
                sum+=1
            else:
                sum+=decode(msg[2:])#recursively call with remainder
    return sum
