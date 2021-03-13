
def printProblem():
    print("This problem was asked by Facebook.\n"
            "  Given the mapping a = 1, b = 2, ... z = 26, and an encoded\n"
            "  message, count the number of ways it can be decoded.\n"
            "  For example, the message '111' would give 3, since it could be\n"
            "  decoded as 'aaa', 'ka', and 'ak'.\n"
            "  You can assume that the messages are decodable. For example,\n"
            "  /'001/' is not allowed.")
# 1   a
# 2   b
# 3   c
# 4   d
# 5   e
# 6   f
# 7   g
# 8   h
# 9   i
# 10  j
# 11  k
alphaSet=set()
for i in range(0,27):
    alphaSet.add(str(i))

def decode(msg,decodeSet=alphaSet):
    if len(msg)==0:
        return 1
    oneLetterVal=msg[0]
    sum=0
    if oneLetterVal in decodeSet:
        if len(msg)==1:
            sum+=1
        else:
            sum+=decode(msg[1:])#recursively call with remainder
    if len(msg)>=2:
        twoLetterVal=msg[:2]
        if twoLetterVal in decodeSet:
            if len(msg)==2:
                sum+=1
            else:
                sum+=decode(msg[2:])#recursively call with remainder
    return sum
import unittest
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(1,decode("1"))
        self.assertEqual(1,decode("2"))
        self.assertEqual(1,decode("3"))
        self.assertEqual(1,decode("4"))
        self.assertEqual(1,decode("5"))
        self.assertEqual(1,decode("6"))
        self.assertEqual(1,decode("7"))
        self.assertEqual(1,decode("8"))
        self.assertEqual(1,decode("9"))
        self.assertEqual(2,decode("10"))
        self.assertEqual(2,decode("11"))
        self.assertEqual(2,decode("12"))
        self.assertEqual(2,decode("13"))
        self.assertEqual(2,decode("14"))
        self.assertEqual(2,decode("15"))
        self.assertEqual(2,decode("16"))
        self.assertEqual(2,decode("17"))
        self.assertEqual(2,decode("18"))
        self.assertEqual(2,decode("19"))
        self.assertEqual(2,decode("20"))
        self.assertEqual(2,decode("21"))
        self.assertEqual(2,decode("22"))
        self.assertEqual(2,decode("23"))
        self.assertEqual(2,decode("24"))
        self.assertEqual(2,decode("25"))
        self.assertEqual(2,decode("26")) #b+f, z
        self.assertEqual(1,decode("27")) #b+f, z
        self.assertEqual(3,decode("111"))
        self.assertEqual(3,decode("126"))
        self.assertEqual(2,decode("127")) #1,2,7 , 12,7, 1,27 fails!

if __name__=="__main__":
    unittest.main()
