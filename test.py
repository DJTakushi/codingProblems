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
            print i
    return problemLines

def testMake(problemDir):
    os.system("cmake "+problemDir+"/CMakeLists.txt")
    os.system("cd "+problemDir)
    os.system("make -C " + problemDir)
    print("done with testMake")

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
        sys.path.insert(1,problemDir) #add directory to paths
        import testLocal
        os.chdir(problemDir) #change to testLocal dir to use relative paths
        print(testLocal.testSolution())
        os.chdir("..")#return to calling directory

def getTestDirectories():
    testDirs = [] #add test directories here
    testDirs.append("dc55")
    #testDirs.append("dc55_2")
    return testDirs
def buildAll():
    testDirs = getTestDirectories()
    for i in testDirs:
        getProblem(i)
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
