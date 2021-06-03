class sLog:
    def __init__(self):
        self.orderList=list()
    def record(self,id):
        self.orderList.append(id)
    def get_last(self,i):
        idx=len(self.orderList)-i
        if idx < 0:
            return -1
        return self.orderList[idx]
