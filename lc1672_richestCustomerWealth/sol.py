# https://leetcode.com/problems/richest-customer-wealth/
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
#
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

class Solution:
    def maximumWealth(self, accounts) -> int:
        o = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum+=j
            if o < sum:
                o = sum
        return o

if __name__=="__main__":
    sol = Solution()
    assert 6 == sol.maximumWealth([[1,2,3,],[3,2,1]])
    assert 10 == sol.maximumWealth([[1,5],[7,3],[3,5]])
    assert 17 == sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])
