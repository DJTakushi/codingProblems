import os
import ctypes

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
    libc_main = ctypes.CDLL("/codingProblems/dc55/libmain_lib.so")

    #helpful!
    #https://stackoverflow.com/questions/13445568/python-ctypes-how-to-free-memory-getting-invalid-pointer-error
    libc_main.unitTest.restype = ctypes.c_void_p
    ptr = libc_main.unitTest()
    print("    In Python: unitTest returns \""+ str(ctypes.cast(ptr,ctypes.c_char_p).value) + "\"")
    print("    pointer = "+hex(ptr))
    libc_main.freeme.argtypes = ctypes.c_void_p,
    libc_main.freeme(ptr)

def sample():
    problemDir = "dc55"
    getProblem(problemDir)
    testMake(problemDir)
    unitTest(problemDir) #currently breaks with the current return type

sample()
