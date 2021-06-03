

def maxFilePathLen(fs):
    fs=preprocess(fs)
    recordString = ""
    path=list()
    eList=fs.split('\\')
    while len(eList) != 0:
        if len(path)==0:
            path.append(eList.pop(0))
        level=0
        while eList[0] == "n" or eList[0] == "t":#get level from markers
            eList.pop(0)
            level+=1
        while len(path)>level: #trim current path until appropriate
            path.pop(-1)
        name=eList.pop(0)
        name=name[1:] #get rid of starting t
        path.append(name)
        if "." in name:
            fileString=""
            for i in range(len(path)):
                fileString+=path[i]
                if i < len(path)-1:
                    fileString+="/"
            if len(fileString)>len(recordString):
                recordString=fileString
    return len(recordString)

def preprocess(input):
    input=input.replace("\n","\\n")
    input=input.replace("\t","\\t")
    return input
