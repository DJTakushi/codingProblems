def printProblem():
    print("Daily Coding Problem: Problem #21 [Easy]\n"
            "This problem was asked by Snapchat.\n"
            "Given an array of time intervals (start, end) for classroom\n"
            "lectures (possibly overlapping), find the minimum number of rooms\n"
            "required.\n"
            "For example, given [(30, 75), (0, 50), (60, 150)], you should\n"
            "return 2.")

class classRoom:
    def __init__(self,classSession):
        self.classes=list()
        self.classes.append(classSession)
    def canAdd(self,interval):
        for classSession in self.classes:
            if interval[0] > classSession[0] and interval[0] < classSession[1]:
                return False
            if interval[1] > classSession[0] and interval[1] < classSession[1]:
                return False
        return True

class classRoomManager:
    def __init__(self,classSessionList=None):
        self.classRoomList=list()
        if classSessionList:
            for classSession in classSessionList:
                self.addClass(classSession)
    def addClass(self,classSession):
        for myClassRoom in self.classRoomList:
            if myClassRoom.canAdd(classSession):
                myClassRoom.classes.append(classSession)
                return
        self.classRoomList.append(classRoom(classSession))
    def getClassRoomQuanity(self):
        return len(self.classRoomList)


import unittest
class myTest(unittest.TestCase):
    def testThis(self):
        cmm=classRoomManager([(30,75),(0,50),(0,150)])
        self.assertEqual(2,cmm.getClassRoomQuanity())
if __name__=="__main__":
    unittest.main()
