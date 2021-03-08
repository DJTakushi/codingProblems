import unittest
class tData:
    def print(self):
        for key,value in vars(self).items():
            print("  "+key+ " = "+str(value))
class testCase:
    def __init__(self,data,expectation):
        self.data=data
        self.expectation=expectation
    def print(self):
        self.data.print()
        print("  expectation = "+str(self.expectation))
class tunittest(unittest.TestCase):
    def test_executeTests(self):
        for test in self.makeTestVector():
            result=functionWrapper(test.data)
            if result != test.expectation:
                print("FAIL!!! For test case: ")
                test.print()
                print("  received "+str(result))
            self.assertEqual(test.expectation, result)
def test(testFunctionW,testVector):
    for test in testVector:
        result=testFunctionW(test.data)
        if result != test.expectation:
            print("FAIL!!! For test case: ")
            test.print()
            print(" received "+str(result))
            return False
    print(" pass.")
    return True
