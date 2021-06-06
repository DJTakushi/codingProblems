import ctypes,os,sys,unittest,testHelper
def configureSolutionLibrary():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    solutionPath = dirpath+"/solution.so"
    myLib=ctypes.cdll.LoadLibrary(solutionPath)
    myLib.createUrlManager.restype = ctypes.c_void_p
    myLib.shorten.argTypes = [ctypes.c_void_p,ctypes.c_char_p]
    myLib.shorten.restype = ctypes.c_void_p

    myLib.restore.argTypes = [ctypes.c_void_p,ctypes.c_char_p]
    myLib.restore.restype = ctypes.c_void_p

    myLib.deleteUrlManager.argTypes = [ctypes.c_void_p]
    myLib.freeCharPtr.argtypes = [ctypes.c_void_p]
    return myLib
class myTest(unittest.TestCase):
    def testThis(self):
        myLib = configureSolutionLibrary()
        myUrlManager= ctypes.c_void_p(myLib.createUrlManager())

        stringList = list()
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

        for i in stringList:
          shortened = myLib.shorten(myUrlManager, i)
          shortenedString = ctypes.cast(shortened,ctypes.c_char_p).value
          restored = myLib.restore(myUrlManager, shortenedString)
          restoredString = ctypes.cast(restored,ctypes.c_char_p).value
          self.assertEqual(i,restoredString)
          myLib.freeCharPtr(shortened)
          myLib.freeCharPtr(restored)
        myLib.deleteUrlManager(myUrlManager)
def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
