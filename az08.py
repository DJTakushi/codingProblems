def reverse_words_OLD(sentence):#simple string manipulation.
#probably higher memory usage though and doesn't use a list of characters like the prompt mentions
    pythonString=False
    if pythonString:
        wordList=sentence.split(" ")
        output=""
        for iter in wordList:
            if output=="":
                output=iter
            else:
                output=iter+" "+output
        return output
    else:
        return sentence
def reverse_words(sentence):
    charray=strTocharray(sentence)
    charray=reverseStringSection(charray,0,len(charray)-1)
    endIdx=0
    startIdx=0
    while endIdx < len(charray):
        #print("startIdx="+str(startIdx)+" endIdx="+str(endIdx))
        flipFlag=False
        if endIdx+1==len(charray):
            flipFlag=True
        else:
            if charray[endIdx+1]==" ":
                flipFlag=True
        if flipFlag:
            #print("FLIPPING at startIdx="+str(startIdx)+" and endIdx="+str(endIdx))
            reverseStringSection(charray,startIdx,endIdx)
        if(charray[endIdx-1]==" "):
            startIdx=endIdx
        endIdx+=1
        #print(charray)
    newSentence=charrayToStr(charray)
    return newSentence

def reverseStringSection(string,startIdx,endIdx):
    if string==None:
        return string
    if endIdx>=len(string):
        return string
    offset=0
    sidx=startIdx
    eidx=endIdx
    while sidx < eidx:
        temp=string[eidx]
        string[eidx]=string[sidx]
        string[sidx]=temp
        sidx+=1
        eidx-=1
    #print(charrayToStr(string,startIdx,endIdx))
    return string

def strTocharray(string):
    return [char for char in string]

def charrayToStr(charray, startIdx=0,endIdx=None):
    output=""
    idx=startIdx
    if endIdx:
        finalIdx=endIdx
    else:
        finalIdx=len(charray)-1
    while idx <= finalIdx:
        output+=charray[idx]
        idx+=1
    return output

def test_reverse_words():
    tests=[("We love Python","Python love We")]
    tests.append(("World Hello","Hello World"))
    tests.append(("To be or not to be","be to not or be To"))
    tests.append(("You are amazing","amazing are You"))
    for iter in tests:
        product=reverse_words(iter[0])
        if iter[1]==product:
            print("Pass.")
        else:
            print("FAIL!  Expected \""+iter[1]+"\" but received \""+product+"\"")
test_reverse_words()
