# az14. Find Low/High Index
Given a sorted array of integers, return the low and high index of the given key. You must return -1 if the indexes are not found. The array length can be in the millions with many duplicates.  Consider the Array:
 - IDX[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10]
 - VAL 1   2   5   5   5   5   5   5   5   5   20
In the above example, according to the key, the low and high indices would be:
- key: 1, low = 0 and high = 0
 - key: 2, low = 1 and high = 1
 - key: 5, low = 2 and high = 9
 - key: 20, low = 10 and high = 10
## Performance
 - Runtime Complexity: Logarithmic, O(logn)
 - Memory Complexity: Constant, O(1)")
## https://www.educative.io/blog/crack-amazon-coding-interview-questions
