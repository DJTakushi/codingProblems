# Given an integer num, return the number of steps to reduce it to zero.
#
# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.


class Solution:
    def numberOfSteps(self, num: int) -> int:
        o = 0
        while num!= 0:
            if num%2==0:
                num/=2
            else:
                num-=1
            o+=1
        return o

if __name__=="__main__":
    sol = Solution()

    assert 6 == sol.numberOfSteps(14)
    assert 4 == sol.numberOfSteps(8)
    assert 12 == sol.numberOfSteps(123)
