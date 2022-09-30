'''
Tranpose these
a,b,c,d
1,2,3,4

a,1
b,2
c,3
d,4


a = ['a','b','c','d']
b = ['1','2','3','4']

def transpose(a,b):
    o = []
    if len(a)==len(b):
        i = 0
        while i < len(a):
            tL=[]
            tL.append(a[i])
            tL.append(b[i])
            o.append(tL)
            i+=1
    return o

hinted that the best solution used Pandas, but was understanding when I said that I hadn't used it much
print(transpose(a,b))'''

class parkingGarge:
    def __init__(self, levels, spacesPerLevel):
        self.levels=levels
        self.spacesPerLevel=spacesPerLevel

    def parkCar(self, car):

    def spaceAvailable(self):

    def unParkCar(self, car):

    def getTimeOfParkedCar(self,car):

    def getChargeToUnparkCar(self,car):

class vehicle:
    def __init__(self, parkTime):
        self.parkTime = parkTime

class car(vehicle):
    def getCharge(self):
class bike(vehicle):
    def getCharge(self):
class truck(vehicle):
    def getCharge(self):


pg=parkingGarge()
