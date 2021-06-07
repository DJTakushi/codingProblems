import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import az11
        class myTestCase():
            def __init__(self,v,expected):
                self.v = v
                self.expected = expected
        tv=list()
        tv.append(myTestCase([2,3,4],[set(), {2}, {3}, {2, 3}, {4}, {2, 4}, {3, 4}, {2, 3, 4}]))
        tv.append(myTestCase([2,5,7],[set(), {2}, {5}, {2, 5}, {7}, {2, 7}, {5, 7}, {2, 5, 7}]))
        for i in tv:
            thisResult=[]
            thisResult= az11.get_all_subsets(i.v,thisResult)
            self.assertEqual(i.expected,thisResult)
if __name__=="__main__":
    unittest.main()
