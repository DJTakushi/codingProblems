class node:
    def __init__(self,remainder,value=None):
        self.value=value
        if self.value==None:
            self.value=""#difficult to work with None later
        self.children=dict() #key = letter, child node
        self.terminator=False #is this a terminator for a word?
        if remainder == "":
            self.terminator=True
        else:
            self.add(remainder)
    def add(self,inString):
        if not inString:
            return
        letter=inString[0]
        remainder=inString[1:]
        if letter in self.children.keys():
            self.children[letter].add(remainder)
        else:
            self.children[letter]=node(remainder,letter)
    def getAll(self, filterString=None):
        thisLetter,thisRemainder=None,None
        if filterString:
            if len(filterString)>0:
                thisLetter=filterString[0]
            if len(filterString)>1:
                thisRemainder=filterString[1:]

        theList=list()
        if self.terminator:
            theList.append(self.value)#add just the value
        applicableValues=list()
        if filterString:
            if thisLetter in self.children.keys():
                applicableValues.append(self.children[thisLetter])
        else:
            applicableValues=self.children.values()

        for i in applicableValues:
            childList=i.getAll(thisRemainder)
            for j in childList:
                theList.append(self.value+j)
        return theList
