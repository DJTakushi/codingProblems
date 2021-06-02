# DC 04
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well. For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.  You can modify the input array in-place.
 - https://stackoverflow.com/questions/51346136/given-an-array-of-integers-find-the-first-missing-positive-integer-in-linear-ti

## Fibonocci?
- [1,2,0]
  | number |  Sum  |   Fibonocci |
  | ---    | ---   | ---         |
  | 1      |1      | 1           |
  | 2      |3      | 3           |
  | 0      |3      | 3   *ignore 0.  If equal, missing the next one |
- [3,4,-1,1]
  | number | Sum     |Fibonocci |
  | ---    | ---     |          |
  | 3      | 3       |1         |
  | 4      | 7       |3         |
  | -1     | 3       |3   *ignore negatives, duplicates, and zeros|
  | 1      | 8       |6   difference is 2.  2 is missing|
- 3   4   -1  1
 [0] 1   3   4 : ordered list withot negatives can be traversed to find that index and value doesn't  - ---- checkMatches
 - first remove negatives:
 - 3   4   0   1
 - flip to negative to serve as a flag
 - -3  -4  0   -1
 Apply order by
 - replacing swapping each element into the appropriate index (if it exists)
  - if the target is the same value, zero this value
    - if this value is negative, zero it.
 |3  | 4 |  -1 | 1 | Strategy  |
 | - | - | --- | - | --- |
 |1  | 4 |  -1 | 3 |  swap i[0] and i[3]|
 |4  | 1 |  -1 | 3 |  swap i[0] and i[1]|
 |0  | 1 |  -1 | 3 |  swap i[0] and i[4] (DNE, so 0)|
 |0  | 1 |  -1 | 3 |  i[1] = 1, so do nothing|
 |0  | 1 |  0  | 3 |  i[2] is negative, so zero it |
 |0  | 1 |  0  | 3 |  i[3] is 3, so do nothing |


| -1 |-2 |  3 |  3 |  2 |  4 | |
| -- | - | -- | -- | -- | -- | |
| 0  |-2 |  3 |  3 |  2 |  4 |  i[0] negative, so zero it|
| 0  | 0 |  3 |  3 |  2 |  4 |  i[1] negative, so zero it|
| 0  | 0 |  0 |  3 |  2 |  4 |  swap i[2] and i[3], but since they're the same, zero i[2] |
| 0  | 0 |  0 |  3 |  2 |  4 |  i[3] is 3, so do nothing |
| 0  | 0 |  2 |  3 |  0 |  4 |  swap i[2] with i[4] |
| 0  | 0 |  2 |  3 |  0 |  4 |  i[4] is 4, so we're Good |
