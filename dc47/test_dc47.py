import ctypes,os,unittest
def configureSolutionLibrary():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    solutionPath = dirpath+"/solution.so"
    myLib=ctypes.cdll.LoadLibrary(solutionPath)
    myLib.myFunctionArray.argTypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    myLib.myFunctionArray.restype = ctypes.c_int
    return myLib
class myTest(unittest.TestCase):
    def test1(self):
        myLib = configureSolutionLibrary()
        input = [9, 11, 8, 5, 7, 10]
        expectation = 5

        seq = ctypes.c_int * len(input)
        arr = seq(*input)

        result =myLib.myFunctionArray(arr,len(input))
        self.assertEqual(expectation, result)
    def test2(self):
        myLib = configureSolutionLibrary()
        input = [9, 11, 8, 5, 7, 10,11]
        expectation = 6
        seq = ctypes.c_int * len(input)
        arr = seq(*input)

        result =myLib.myFunctionArray(arr,len(input))
        self.assertEqual(expectation, result)
    def test3(self):
        myLib = configureSolutionLibrary()
        input = [9, 11, 8, 5, 7, 10,11,0,15]
        expectation = 15
        seq = ctypes.c_int * len(input)
        arr = seq(*input)

        result =myLib.myFunctionArray(arr,len(input))
        self.assertEqual(expectation, result)
if __name__=="__main__":
    unittest.main()
