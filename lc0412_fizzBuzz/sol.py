# https://leetcode.com/problems/fizz-buzz/
# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#

class Solution:
    def fizzBuzz(self, n: int):
        o = []
        for i in range(1,n+1):
            to = ""
            d3 = i%3==0
            d5 = i%5==0
            if d3 and d5:
                to = "FizzBuzz"
            elif d3:
                to="Fizz"
            elif d5:
                to = "Buzz"
            else:
                to = str(i)
            o.append(to)
        return o

if __name__=="__main__":
    sol = Solution()

    o = sol.fizzBuzz(3)
    # print(o)
    assert len(o) == 3
    assert o[0] == "1"
    assert o[1] == "2"
    assert o[2] == "Fizz"

    o = sol.fizzBuzz(5)
    assert len(o) == 5
    assert o[0] == "1"
    assert o[1] == "2"
    assert o[2] == "Fizz"
    assert o[3] == "4"
    assert o[4] == "Buzz"

    o = sol.fizzBuzz(15)
    assert len(o) == 15
    assert o[0] == "1"
    assert o[1] == "2"
    assert o[2] == "Fizz"
    assert o[3] == "4"
    assert o[4] == "Buzz"
    assert o[5] == "Fizz"
    assert o[6] == "7"
    assert o[7] == "8"
    assert o[8] == "Fizz"
    assert o[9] == "Buzz"
    assert o[10] == "11"
    assert o[11] == "Fizz"
    assert o[12] == "13"
    assert o[13] == "14"
    assert o[14] == "FizzBuzz"
