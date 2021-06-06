import ctypes,os,sys,unittest,testHelper
def configureSolutionLibrary():
    dirpath = os.path.dirname(os.path.abspath(__file__))
    solutionPath = dirpath+"/solution.so"
    myLib=ctypes.cdll.LoadLibrary(solutionPath)

    myLib.node_new.argTypes = [ctypes.c_void_p, ctypes.c_char_p]
    myLib.node_new.restype = ctypes.c_void_p

    myLib.node_setL.argTypes = [ctypes.c_void_p,ctypes.c_void_p] #pointer to node
    myLib.node_setL.restype = ctypes.c_void_p

    myLib.node_setR.argTypes = [ctypes.c_void_p,ctypes.c_void_p] #pointer to new node
    myLib.node_setR.restype = ctypes.c_void_p

    myLib.node_getL.argTypes = [ctypes.c_void_p,ctypes.c_void_p] #pointer to new node
    myLib.node_getL.restype = ctypes.c_void_p

    myLib.node_getR.argTypes = [ctypes.c_void_p,ctypes.c_void_p] #pointer to new node
    myLib.node_getR.restype = ctypes.c_void_p

    myLib.node_getVal.argTypes = [ctypes.c_void_p]
    myLib.node_getVal.restype = ctypes.c_char_p

    myLib.myFunction.argTypes = [ctypes.c_void_p,ctypes.c_void_p] #pointer to head node
    myLib.myFunction.argTypes = ctypes.c_int
    return myLib

myLib = configureSolutionLibrary()
def nn(val):
    return ctypes.c_void_p(myLib.node_new(val))
def sl(h,n):
    myLib.node_setL(h,n)
def sr(h,n):
    myLib.node_setR(h,n)
def gl(h):
    return ctypes.c_void_p(myLib.node_getL(h))
def gr(h):
    return ctypes.c_void_p(myLib.node_getR(h))


class myTest(unittest.TestCase):
    def testThis(self):
        head = nn("*")
        sl(head,nn("+"))
        sr(gl(head),nn("2"))
        sl(gl(head),nn("3"))
        sr(head,nn("+"))
        sl(gr(head),nn("4"))
        sr(gr(head),nn("5"))
        self.assertEqual(45, myLib.myFunction(head))


        head = nn("/")
        sl(head,nn("-"))
        sl(gl(head),nn("556"))
        sr(gl(head),nn("223"))
        sr(head,nn("+"))
        sl(gr(head),nn("762"))
        sr(gr(head),nn("308"))
        self.assertEqual(0, myLib.myFunction(head))

        head = nn("*")
        sl(head,nn("-"))
        sl(gl(head),nn("556"))
        sr(gl(head),nn("223"))
        sr(head,nn("+"))
        sl(gr(head),nn("762"))
        sr(gr(head),nn("308"))
        self.assertEqual(356310,myLib.myFunction(head))

def runTest():
    return testHelper.testSolution(myTest)
if __name__=="__main__":
    print(runTest())
