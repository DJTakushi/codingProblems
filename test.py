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
    #https://stackoverflow.com/questions/3197509/redirecting-stdio-from-a-command-in-os-system-in-python
    if os.path.isfile(cmakeFilePath):
        from subprocess import Popen, PIPE
        #os.system("cmake "+cmakeFilePath)
        p = Popen(['cmake','CMakeLists.txt'], cwd=dirpath,stdout=PIPE, stderr=PIPE, stdin=PIPE)
        output = p.stdout.read()
        print(output)

        #os.system("make -C " + problemDir)
        p = Popen(['make'], cwd=dirpath, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        output += p.stdout.read()
        print(output)

        print("done with testMake")
    else:
        print("no "+ cmakeFilePath + "; assuming python solution")
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def unitTest(problemDir):
    useCppUnitTest = False
    if useCppUnitTest:
        libc_main = ctypes.CDLL("/codingProblems/dc55/libmain_lib.so")

        libc_main.unitTest.restype = ctypes.c_void_p
        ptr = libc_main.unitTest()
        print("    In Python: unitTest returns \""+ str(ctypes.cast(ptr,ctypes.c_char_p).value) + "\"")
        print("    pointer = "+hex(ptr))
        libc_main.freeme.argtypes = ctypes.c_void_p,
        libc_main.freeme(ptr)
    else:
        sys.path.insert(1,os.getcwd()+"/"+problemDir) #add directory to paths
        import testLocal
        os.chdir(problemDir) #change to testLocal dir to use relative paths
        print(testLocal.testSolution())
        os.chdir("..")#return to calling directory

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
