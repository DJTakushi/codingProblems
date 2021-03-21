def printProblem():
    print("Problem #14 [Medium]\n"
            "This problem was asked by Google.\n"
            "The area of a circle is defined as πr^2. Estimate π to 3\n"
            "decimal places using a Monte Carlo method.\n"
            "Hint: The basic equation of a circle is x2 + y2 = r2.")
# Area of circle is pi*r^2
# Area of square that circumscribes this is (r*2)^2=4r^2
# A_circle/A_square = (pi*r^2)/(4r^2)
# (A_circle/A_square)*4=pi
# In quadrant I of unit circle, y = sqrt(1-x^2)
def getPiMonteCarlo(points):
    from random import random
    class point:
        def __init__(self):
            self.x=random()
            self.y=random()
            self.inCircle=False
            if self.y <= circleY(self.x):
                self.inCircle=True
    circlePoints=0
    for i in range(points):
        thisPoint=point()
        if thisPoint.inCircle: circlePoints+=1
    myPi=4*(circlePoints/points)
    print(myPi)
    return myPi

def circleY(x):
    import math
    y = math.sqrt(1-(x*x))
    return y

import unittest
class myTests(unittest.TestCase):
    def testThis(self):
        myPi = getPiMonteCarlo(1000000)
        for i in range(10):#test this ten times for good measure.
            self.assertTrue(3.13 < myPi and myPi < 3.15)

if __name__=="__main__":
    unittest.main()
