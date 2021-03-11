def printProblem():
    print("This problem was asked by Jane Street.\n"
            "cons(a, b) constructs a pair, and car(pair) and cdr(pair)\n"
            "returns the first and last element of that pair. For example,\n"
            "car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.\n"
            "Given this implementation of cons:\n"
            "  def cons(a, b):\n"
            "      def pair(f):\n"
            "          return f(a, b)\n"
            "      return pair\n"
            "Implement car and cdr.")

def demo():
    #brain farted on this, so I looked it up
    #https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python
    #can access variables using the closure namespace
    #
    def foo():
        spam="Vikings"
        def bar():
            return spam
        return bar
    print(foo)
    print(foo())
    print(foo().__closure__)
    print(foo().__closure__[0].cell_contents)
    print(foo()())

def car(pair):
    def getPairfirst(a,b):
        return a
    return pair(getPairfirst)
def cdr(pair):
    def getPairSecond(a,b):
        return b
    return pair(getPairSecond)


def cons(a, b):
    def pair(f):
       return f(a, b)
    return pair

import unittest
class myTest(unittest.TestCase):
    def test_this(self):
        self.assertEqual(3,car(cons(3,4)))
        self.assertEqual(4,cdr(cons(3,4)))
        self.assertEqual(0,car(cons(0,"viking")))
        self.assertEqual("viking",cdr(cons(0,"viking")))

if __name__=="__main__":
    unittest.main()
