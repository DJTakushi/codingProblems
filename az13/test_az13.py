import os,sys,unittest,importlib
class myTest(unittest.TestCase):
    def testThis(self):
        import az13
        n0=az13.Node(0)
        n1=az13.Node(1)
        n2=az13.Node(2)
        n3=az13.Node(3)
        n4=az13.Node(4)
        n0.neighbors=[n2,n3,n4]
        n1.neighbors=[n2]
        n2.neighbors=[n0]
        n3.neighbors=[n2]
        n4.neighbors=[n0,n1,n3]
        self.assertEqual(True, az13.compareNodeNetworks(n0,az13.clone(n0)))

        n0=az13.Node(0)
        n1=az13.Node(1)
        n2=az13.Node(2)
        n3=az13.Node(3)
        n4=az13.Node(4)
        n5=az13.Node(5)
        n6=az13.Node(6)
        n0.neighbors=[n4,n5,n2,n1,n6,n3]
        n1.neighbors=[n5,n2,n0,n4,n6]
        n2.neighbors=[n5,n4,n1,n0,n3]
        n3.neighbors=[n4,n2,n5,n6,n0]
        n4.neighbors=[n0,n2,n3,n5,n6,n1]
        n5.neighbors=[n1,n2,n0,n4,n3]
        n6.neighbors=[n0,n4,n3,n1]
        self.assertEqual(True, az13.compareNodeNetworks(n0,az13.clone(n0)))
if __name__=="__main__":
    unittest.main()
