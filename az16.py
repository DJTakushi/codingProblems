#https://www.dailycodingproblem.com/
def printProblem():
    print("There's a staircase with N steps, and you can climb 1 or 2 steps\n"
            "at a time. Given N, write a function that returns the number of\n"
            "unique ways you can climb the staircase.\n"
            "The order of the steps matters.\n"
            "For example, if N is 4, then there are 5 unique ways:\n"
            "   1, 1, 1, 1\n"
            "   2, 1, 1\n"
            "   1, 2, 1\n"
            "   1, 1, 2\n"
            "   2, 2\n"
            "What if, instead of being able to climb 1 or 2 steps at a time,\n"
            "you could climb any number from a set of positive integers X?\n"
            "For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps\n"
            "at a time. Generalize your function to take in X.")

def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a
print(str(staircase(1)))
print(str(staircase(2)))
print(str(staircase(3)))
print(str(staircase(4)))
