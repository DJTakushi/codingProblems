import ctypes,os,sys,unittest
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
    def test_1(self):
        head = nn(b'*')
        sl(head,nn(b'+'))
        sr(gl(head),nn(b'2'))
        sl(gl(head),nn(b'3'))
        sr(head,nn(b'+'))
        sl(gr(head),nn(b'4'))
        sr(gr(head),nn(b'5'))
        self.assertEqual(45, myLib.myFunction(head))

    def test_2(self):
        head = nn(b'/')
        sl(head,nn(b'-'))
        sl(gl(head),nn(b'556'))
        sr(gl(head),nn(b'223'))
        sr(head,nn(b'+'))
        sl(gr(head),nn(b'762'))
        sr(gr(head),nn(b'308'))
        self.assertEqual(0, myLib.myFunction(head))

    def test_3(self):
        head = nn(b'*')
        sl(head,nn(b'-'))
        sl(gl(head),nn(b'556'))
        sr(gl(head),nn(b'223'))
        sr(head,nn(b'+'))
        sl(gr(head),nn(b'762'))
        sr(gr(head),nn(b'308'))
        self.assertEqual(356310,myLib.myFunction(head))
if __name__=="__main__":
    unittest.main()
