# AZ 16
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase.  The order of the steps matters.  For example, if N is 4, then there are 5 unique ways:
 1. 1, 1, 1, 1
 2. 2, 1, 1
 3. 1, 2, 1
 4. 1, 1, 2
 5. 2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?  For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.")


# look at cases:
 1. N = 1: [1] (1)
 2. N = 2: [1, 1], [2] (2)
 3. N = 3: [1, 2], [1, 1, 1], [2, 1] (3)
 4. N = 4: [1, 1, 2], [2, 2], [1, 2, 1], [1, 1, 1, 1], [2, 1, 1] (5)
Note that the trend is f(n)=f(n-1)+f(n-2).  This makes sense since in n-1 and n-2, the n-x evalutaion represents the combo that will simply have x added to them at the end.  This allows us to evaulate a funtion at a lower order, which will be easier.

#https://www.dailycodingproblem.com/
