import os
import ctypes
import sys
def getProblem(problemDir):
    filePath = problemDir+"/readme.md"
    with open(filePath) as f:
        fileLines = f.readlines()
        problemLines = []
        for i in fileLines:
            if "##" in i: ##get lines until the '##' in the next .md header
                break
            thisLine = i.replace('\r','').replace('\n','')
            if len(thisLine) > 0:
                if thisLine[0] == '#':
                    thisLine = thisLine[2:] #clip beginning header formatting
            problemLines.append(thisLine)
        for i in problemLines:
            print(i)
    return problemLines

def testMake(problemDir):
    dirpath = os.path.dirname(os.path.abspath(__file__))+'/'+problemDir
    testLogFilePath = dirpath+'/build.stdout.log'
    sys.stdout = open(testLogFilePath, "w")

    cmakeFilePath = problemDir+"/CMakeLists.txt"
    if os.path.isfile(cmakeFilePath):
        from subprocess import Popen, PIPE
        p = Popen(['cmake','CMakeLists.txt'], cwd=dirpath,stdout=PIPE, stderr=PIPE, stdin=PIPE)
        output = p.stdout.read()

        p = Popen(['make'], cwd=dirpath, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        output += p.stdout.read()
        print(output)
        print("done with testMake")
    else:
        print("no "+ cmakeFilePath + "; assuming python solution")
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def unitTest(problemDir):
    relaventDir = os.getcwd()+"/"+problemDir
    libName = problemDir+'.testLocal'
    import importlib
    myLib = importlib.import_module(libName)
    testReturn = myLib.runTest()
    print(testReturn + " "+problemDir)

def getTestDirectories():
    testDirs = [] #add test directories here
    testDirs.append("az01")
    testDirs.append("dc55")
    return testDirs
def buildAll():
    testDirs = getTestDirectories()
    for i in testDirs:
        #sgetProblem(i)
        testMake(i)
def testAll():
    testDirs = getTestDirectories()
    for i in testDirs:
        unitTest(i)
def buildAllTestAll():
    buildAll()
    testAll()
if __name__=="__main__":
    buildAllTestAll()
