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
    testDirs.append("az02")
    testDirs.append("az03")
    testDirs.append("az04")
    testDirs.append("az05")
    testDirs.append("az06")
    testDirs.append("az07")
    testDirs.append("az08")
    testDirs.append("az09")
    testDirs.append("az10")
    testDirs.append("az11")
    testDirs.append("az12")
    testDirs.append("az13")
    testDirs.append("az14")
    testDirs.append("az15")
    testDirs.append("az16")
    testDirs.append("eu01")
    testDirs.append("eu02")
    testDirs.append("eu04")

    testDirs.append("dc01")
    testDirs.append("dc02")
    testDirs.append("dc03")
    testDirs.append("dc04")
    testDirs.append("dc05")
    testDirs.append("dc06")
    testDirs.append("dc07")
    testDirs.append("dc08")
    testDirs.append("dc09")

    #testDirs.append("dc10") #currently not working
    #testDirs.append("dc11") #currently fails
    #testDirs.append("dc12") #currently not startec
    #testDirs.append("dc13") #test fails
    testDirs.append("dc14")
    #testDirs.append("dc15") #unimplemented
    testDirs.append("dc16")
    testDirs.append("dc17")
    testDirs.append("dc18") #impractical solution
    #testDirs.append("dc19") #fails
    testDirs.append("dc20")
    testDirs.append("dc21")
    testDirs.append("dc22")
    testDirs.append("dc23")

    testDirs.append("dc50")
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
