def getPiMonteCarlo(points):
    from random import random
    class point:
        def __init__(self):
            self.x=random()
            self.y=random()
            self.inCircle=False
            if self.y <= circleY(self.x):
                self.inCircle=True
    circlePoints=float(0)
    for i in range(points):
        thisPoint=point()
        if thisPoint.inCircle: circlePoints+=1
    myPi=float(4*circlePoints/points)
    return myPi

def circleY(x):
    import math
    y = math.sqrt(1-(x*x))
    return y
