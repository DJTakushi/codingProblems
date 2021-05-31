# az10
## Given a set of ‘n’ elements, find their Kth permutation.
Consider the following set of elements:
 - [1,2,3]
All permutations of the above elements are (with ordering):
 1. [1,2,3]
 2. [1,3,2]
 3. [2,1,3]
 4. [2,3,1]
 5. [3,1,2]
 6. [3,2,1]
 - Here we need to find the Kth permutation.
 - Runtime Complexity: Linear, O(n)
 - Memory Complexity: Linear, O(n)")
 - https://www.educative.io/blog/crack-amazon-coding-interview-questions

## Their algorithm
If input vector is empty return result vector
 - block_size = (n-1)! ['n' is the size of vector]"
Figure out which block k will lie in and select the first element of that block
 - (this can be done by doing (k-1)/block_size)
 - Append selected element to result vector and remove it from original input vector
 - Deduce from k the blocks that are skipped i.e k = k - selected*block_size and goto step 1)

## SOA Algorithm
 - https://stackoverflow.com/questions/31216097/given-n-and-k-return-the-kth-permutation-sequence
 - Break into sequence
   - To generate these indices, go from right to left and divide k by 1! for the rightmost two places, then 2! then 3! then 4! etc, and then modulo the result with the number of possible indices in that position, which is 1 for the rightmost, 2 for the second-rightmost etc. You don't have to calculate the factorial each time because you can keep a running product.
   - You can break out of the loop as soon as k divided by the factorial is zero, so you only have to compute factorials up until roughly the size of k multiplied by the last place in zwhich k divided by the factorial is non-zero. If k is too large, you need to switch to BigIntegers.
   - Once you have the indices it's pretty straightforward to use them to generate the permutation.
   - For 3 items:
      1. 0 0 0
      2. 0 1 0
      3. 1 0 0
      4. 1 1 0
      5. 2 0 0
      6. 2 1 0
   - For 4 items:
      1. 0 0 0 0
      2. 0 0 1 0
      3. 0 1 0 0
      4. 0 1 1 0
      5. 0 2 0 0
      6. 0 2 1 0

      7. 1 0 0 0
      8. 1 0 1 0
      9. 1 1 0 0
      10. 1 1 1 0
      11. 1 2 0 0
      12. 1 2 1 0

      13. 2 0 0 0
      14. 2 0 1 0
      15. 2 1 0 0
      16. 2 1 1 0
      17. 2 2 0 0
      18. 2 2 1 0

      19. 3 0 0 0
      20. 3 0 1 0
      21. 3 1 0 0
      22. 3 1 1 0
      23. 3 2 0 0
      24. 3 2 1 0
