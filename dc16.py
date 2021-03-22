def printProblem():
    print("Problem #16 [Easy]\n"
            "This problem was asked by Twitter.\n"
            "You run an e-commerce website and want to record the last N\n"
            "order ids in a log. Implement a data structure to accomplish\n"
            "this, with the following API:\n"
            "record(order_id): adds the order_id to the log\n"
            "get_last(i): gets the ith last element from the log. i is\n"
            "guaranteed to be smaller than or equal to N.\n"
            "You should be as efficient with time and space as possible.")

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

import unittest
class myTests(unittest.TestCase):
    def testThis(self):
        slog=sLog()
        slog.record("22")
        slog.record("380")
        slog.record("9")
        slog.record("556")
        self.assertEqual("556",slog.get_last(1))
        self.assertEqual("9",slog.get_last(2))
        self.assertEqual("380",slog.get_last(3))
        self.assertEqual("22",slog.get_last(4))
        self.assertEqual(-1,slog.get_last(5))
        slog.record("762")
        slog.record("6.5")
        slog.record("300")
        slog.record("12.7")
        slog.record("20")

        self.assertEqual("22",slog.get_last(9))
        self.assertEqual("380",slog.get_last(8))
        self.assertEqual("9",slog.get_last(7))
        self.assertEqual("556",slog.get_last(6))
        self.assertEqual("762",slog.get_last(5))
        self.assertEqual("6.5",slog.get_last(4))
        self.assertEqual("300",slog.get_last(3))
        self.assertEqual("12.7",slog.get_last(2))
        self.assertEqual("20",slog.get_last(1))

if __name__=="__main__":
    unittest.main()
