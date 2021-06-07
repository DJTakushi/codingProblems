import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import az10
        class myTestCase():
            def __init__(self,v,k,expected):
                self.v = v
                self.k = k
                self.expected = expected
        tv=list()
        tv.append(myTestCase(["1","2","3"],6,"321"))
        tv.append(myTestCase(["1","2","3","4"],8,"2143"))
        tv.append(myTestCase(["1","2","3","4"],24,"4321"))
        tv.append(myTestCase(["1","2","3","4"],23,"4312"))
        for i in tv:
            thisResult=""
            thisResult= az10.find_kth_permutation(i.v,i.k,thisResult)
            self.assertEqual(i.expected,thisResult)
if __name__=="__main__":
    unittest.main()
