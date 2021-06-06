# dc50
Daily Coding Problem: Problem #50 [Easy] \
This problem was asked by Microsoft. \
Suppose an arithmetic expression is given as a binary tree.  Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'. \
Given the root to such a tree, write a function to evaluate it. \
For example, given the following tree: \
      * \
     / \\ \
    +    + \
   / \\  / \\ \
  3  2  4  5 \

You should return 45, as it is (3 + 2) * (4 + 5).

## Notes
- Looks like ctypes can't use class functions, so additional c-functions are required for use in python
  - https://stackoverflow.com/questions/16268140/python-using-ctypes-to-create-c-class-wrapper
