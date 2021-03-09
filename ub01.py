
def printPrompt():
    print("Given an array of integers, return a new array such that\n"
            "each element at index i of the new array is the product of\n"
            "all the numbers in the original array except the one at i.\n"
            "For example, if our input was [1, 2, 3, 4, 5],\n"
            "the expected output would be [120, 60, 40, 30, 24].\n"
            "If our input was [3, 2, 1], the expected output would be [2, 3, 6].\n"
            "Follow-up: what if you can't use division?")
# Easy appraoch is to calculate the big sum, and then for each index, divide by
# the current index's value.
#If we can't use division, we can perhaps organize it somehow as a tree?
#   0
# 1  5*6*7*8 *3*4 *2
# 2  5*6*7*8 *3*4 *1

# 3  5*6*7*8 *1*2 *4
# 4  5*6*7*8 *1*2 *3

# 5 1*2*3*4 *7*8 *6
# 6 1*2*3*4 *7*8 *5

# 7 1*2*3*4 *5*6 *8
# 8 1*2*3*4 *5*6 *7
