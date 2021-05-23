import ctypes
def configureSolutionLibrary():
    solutionPath = "./solution.so"
    myLib=ctypes.cdll.LoadLibrary(solutionPath)
    myLib.createUrlManager.restype = ctypes.c_void_p
    myLib.shorten.argTypes = [ctypes.c_void_p,ctypes.c_char_p]
    myLib.shorten.restype = ctypes.c_void_p
    myLib.restore.argTypes = [ctypes.c_void_p,ctypes.c_char_p]
    myLib.restore.restype = ctypes.c_void_p
    myLib.deleteUrlManager.argTypes = [ctypes.c_void_p]
    myLib.freeCharPtr.argtypes = [ctypes.c_void_p]
    return myLib
def testSolution():
    myLib = configureSolutionLibrary()
    myUrlManager= ctypes.c_void_p(myLib.createUrlManager())

    stringList = []
    stringList.append("y33t")
    stringList.append("beetz")
    stringList.append("y33t")
    stringList.append("0")
    stringList.append("1")
    stringList.append("4")
    stringList.append("556")
    stringList.append("762")
    stringList.append("762")
    stringList.append("762 SOVIET")

    result = True
    counter = 0
    outString = ""
    for i in stringList:
      shortened = myLib.shorten(myUrlManager, i)
      shortenedString = ctypes.cast(shortened,ctypes.c_char_p).value
      restored = myLib.restore(myUrlManager, shortenedString)
      restoredString = ctypes.cast(restored,ctypes.c_char_p).value
      if i != restoredString:
          result = False
          outString = "Fail at case "+str(counter)+"!  Expected \""+i+"\", but received \""+restoredString+"\"\n";
      myLib.freeCharPtr(shortened)
      myLib.freeCharPtr(restored)
      counter += 1
    if result:
        outString = "Pass!"
    myLib.deleteUrlManager(myUrlManager)
    return outString

if __name__=="__main__":
    print(testSolution())
