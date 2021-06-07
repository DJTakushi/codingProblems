import os,sys,unittest,importlib
import dc16
from random import random
class myTest(unittest.TestCase):
    def test_this(self):
        slog=dc16.sLog()
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

        self.assertEqual(-1,slog.get_last(10))
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
