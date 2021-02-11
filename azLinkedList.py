class LinkedListNode:
    def __init__(self,data,previous=None):
        self.data=data.pop(0)
        self.previous=previous
        self.next=None
        self.arbitrary=None
        if len(data):
            self.next=LinkedListNode(data,self)

    def getData(self):
        return self.data
    def setNext(self, next):
        self.next=next
    def setPrevious(self,previous):
        self.previous=previous
    def getNext(self):
        return self.next
    def getPrevious(self):
        return self.previous
    def returnList(self,outList):
        outList.append(self.data)
        if self.next!=None:
            self.next.returnList(outList)
    def applyArbitrary(self, refList,nodeList=None):
        #refList is a list of which node index should set as the arbitrary for the node
        if not nodeList:
            nodeList=self.getIndexList()
        self.arbitrary=nodeList[refList.pop(0)]
        if self.next:
            self.next.applyArbitrary(refList,nodeList)
        return
    def getDictIndex(self,counter=0,inDict=None):
        #returns dictionary where key is node and value is index
        if inDict==None:
            inDict={}
        inDict[self]=counter
        counter+=1
        if self.next:
            self.next.getDictIndex(counter, inDict)
        return inDict
    def getIndexList(self,inList=None):
        #return a python list where each value is an item in this linked list
        if inList==None:
            inList=[]
        inList.append(self)
        if self.next:
            self.next.getIndexList(inList)
        return inList
    def printRecursive(self, counter=0, nodeIdxDict=None):
        if nodeIdxDict==None:
            nodeIdxDict=self.getDictIndex()
        printString= " node "+str(counter)
        printString+=" value = " + str(self.getData())
        printString+=" abitrary node value = "
        if self.arbitrary:
            printString+=str(nodeIdxDict[self.arbitrary])
        else:
            printString+="blank"
        print(printString)
        if self.next:
            counter+=1
            self.next.printRecursive(counter, nodeIdxDict)
    def exportList(self, outList=None,nodeIdxDict=None):
        if nodeIdxDict==None:
            nodeIdxDict=self.getDictIndex()
        if outList==None:
            outList=[]
        #outputs list of tuples where [0]=node data and [1]=idx of arbitrary
        myTuple=(self.data,nodeIdxDict[self.arbitrary])
        outList.append(myTuple)
        if self.next:
            self.next.exportList(outList,nodeIdxDict)
        return outList
    def checkMatches(self,inputLinkedList):
        myExport=self.exportList()
        inputExport=inputLinkedList.exportList()
        myIdxDict=self.getDictIndex()
        inputIdxDict=inputLinkedList.getDictIndex()
        counter=0
        if len(myExport) != len(inputExport):
            outStr="Input list lenght ("+str(len(inputLinkedList))
            outStr+= ") doesn't match my length ("+str(len(inputLinkedList))+ ")"
            print(outStr)
            return False
        while counter < len(myExport):
            myNode=myExport[counter]
            inputNode=inputExport[counter]
            if(myNode[0] != inputNode[0]):
                outStr="Idx="+str(counter)+": "
                outStr+=" myValue="+str(myNode[0])
                outStr+=" but input value="+str(inputNode[0])
                print(outStr)
                return False
            if(myNode[1] != inputNode[1]):
                outStr="Idx="+str(counter)+": "
                outStr+=" pointer="+str(myNode[1])
                outStr+=" but input pointer="+str(inputNode[1])
                print(outStr)
                return False
            counter+=1
        return True
