class testCase:
    def __init__(self,data,expectation):
        self.data=data
        self.expectation=expectation
    def print(self):
        self.data.print()
        print("  expectation = "+str(self.expectation))
def test(testFunctionW,testVector):
    for test in testVector:
        result=testFunctionW(test.data)
        if result != test.expectation:
            print("FAIL!!! For test case: ")
            test.print()
            print(" received "+str(result))
            return
    print(" pass.")
