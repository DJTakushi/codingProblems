def stringToWordList(wordList,crushedString):
    if crushedString in wordList:
        return [crushedString]
    for i in range(len(crushedString)):
        if crushedString[0:i] in wordList:
            outList=stringToWordList(wordList,crushedString[i:])
            if outList == -1:
                continue
            else:
                outList.insert(0,crushedString[0:i])
                return outList
    return -1
