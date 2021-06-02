# DC08
This problem was asked by Google.
A unival tree (which stands for \"universal value\") is a tree where all nodes under it have the same value.  Given the root
a binary tree, count the number of unival subtrees. \
For example, the following tree has 5 unival subtrees:
-    0
-   / \
-  1   0
-     / \
-    1   0
-   / \
-  1   1
## https://www.dailycodingproblem.com/blog/unival-trees/



   0
  / \
 1   0 

   a
  / \
 a   a
     /\
    a  a
        \
         A
 This tree has 3 unival subtrees: the two ‘a’ leaves and the one ‘A’ leaf. The ‘A’ leaf causes all its parents to not be counted as a unival tree, however.

   a
  / \
 c   b
     /\
    b  b
         \
          b
 This tree has 5 unival subtrees: the leaf at ‘c’, and every ‘b’.
