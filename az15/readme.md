# az15 Search Rotated Array
Search for a given number in a sorted array, with unique elements, that has been rotated by some arbitrary number.  Return [-1] if the number does not exist.  Assume that the array does not contain duplicates.  For example, below is an origianl array before rotation:
 - [0]   [1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]   [9]   [10]  [11]  [12]  [13]  [14]  [15]  [16]  [17]  [18]  [19]
 - [1]   [10]  [20]  [47]  [59]  [63]  [75]  [88]  [99]  [107] [120] [133] [155] [162] [176] [188] [199] [200] [210] [222]
After performign rotatin on this array 6 times, it chagnes to:
 - [0]   [1]   [2]   [3]   [4]   [5]   [6]   [7]   [8]   [9]   [10]  [11]  [12]  [13]  [14]  [15]  [16]  [17]  [18]  [19]
 - [176] [188] [199] [200] [210] [222] [1]   [10]  [20]  [47]  [59]  [63]  [75]  [88]  [99]  [107] [120] [133] [155] [162]
## Performance
 - Runtime Complexity: Logarithmic,O(logn)
 - Memory Complexity: Logarithmic,O(logn))

# Truth Table Strategy
|key<Mid | LSorted  | key>Lmin  | RSorted | key<Rmax  |Dir  |
| ------ | ---------| --------- | ------- | --------- | --- |
|1       |1         |1          |x        |x          |L    |
|1       |1         |0          |x        |x          |R    |
|1       |0         |x          |x        |x          |L    |
|0       |x         |x          |1        |1          |R    |
|0       |x         |x          |1        |0          |L    |
|0       |x         |x          |0        |x          |R    |
#https://www.educative.io/blog/crack-amazon-coding-interview-questions
