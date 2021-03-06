# dc19
Daily Coding Problem: Problem #19 [Medium] \
This problem was asked by Facebook. \
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color. Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

## Notes
 K   0   1   2   3   4   5
 N
 0   x   y   z
 1
 2
 3
 4

 Could naively calculate every permutation and take the min.  Discared ones that
 violate the neighboring k requirement.

 If k is not consistent for each row, I can't think of an iteration pattern that
 could be used.  For example, if we have the table:
 K   0   1   2
 N   1   2   3
 0   1   2   3   0
 1   1   2   3   1
 2   1   2   3   0
 3   1   2   3   1
 4   10  10  2   2

 Actually, this seems do-able
 pre
 1:  select cheapest in N[0]
 2:  loop
     a)select cheapest in new row
     b)if cheapest conflicts with past
         i)calculate alternate
             switch previous index to next cheapest option that is not current selection k idx nor pre-prev kIdx
              Would have to do this for all indeces.  See below


 K   0   1
 N   1   2
 0   1   2   -0- 1
 1   1   2   -1- 0
 2   1   2   -0- 1
 3   1   2   -1- 0
 4   10  2   -0- 1

 K   0   1
 N   1   2               keep    sum
 0   100 2   -0- 1
 1   1   2   -0- 1
 2   1   2   -1- 0
 3   10  2   -0- 1


 Must recursive call a function that gets the minimum while avoiding a last specified index
