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
