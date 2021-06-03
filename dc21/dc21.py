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
