def sumNonAdjNumbers(input):
    #return simpleMethod(input)
    sum,pIdx,ppIdx=input[0],0,-2 #default to take first
    for i in range(1,len(input)):
        if i - pIdx > 1: #add if possible
            sum+=input[i]
            ppIdx=pIdx
            pIdx=i
        else:
            potentialSum=sum-input[pIdx]
            potentialSum+=input[i]
            canUsePIdxM1=False
            if pIdx-1 >=0 and pIdx-1 !=ppIdx+1:
                canUsePIdxM1=True #if we can use the item before the previous, we should.
                potentialSum+=input[pIdx-1]
            if potentialSum > sum:
                if canUsePIdxM1:
                    pIdx-=1
                    ppIdx = pIdx #pp unchanged
                pIdx = i
                sum=potentialSum
    return sum
def simpleMethod(input):
    #calculate each sum and check if it's the good.  If highest record, it's highest.  Completes in 2^n time
    class trial:
        def __init__(self,num,inputArray=None):
            self.num=num
            self.arrBin=list()
            for i in range(len(input)) :
                if num%2==1:
                    self.arrBin.append(True)
                else:
                    self.arrBin.append(False)
                num=num>>1
            self.valid=True
            for i in range(len(self.arrBin)):
                if i > 0:
                    if self.arrBin[i] and self.arrBin[i-1]:
                        self.valid=False
            if inputArray:
                self.getSum(inputArray)
            #self.printTrial()
        def printTrial(self):
            print("num = "+str(self.num))
            print("arrBin = "+str(self.arrBin))
            print("self.valid = "+str(self.valid))
        def getSum(self,inputArray):
            self.sum=0
            for i in range(len(self.arrBin)):
                if self.arrBin[i]:
                    self.sum+=inputArray[i]
    import math
    maxOption=math.pow(2,len(input))

    trialArray=list()
    maxSum = 0
    for i in range(int(maxOption)):
        thisTrial = trial(i,input)
        if thisTrial.valid and thisTrial.sum > maxSum:
            maxSum = thisTrial.sum
    return maxSum
