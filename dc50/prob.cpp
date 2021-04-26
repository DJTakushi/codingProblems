#include <string>
#include <iostream>
#include <vector>
#include "prob.h"
std::string prob(void)
{
  std::string output =
  "Daily Coding Problem: Problem #50 [Easy]\n"
  "This problem was asked by Microsoft.\n"
  "Suppose an arithmetic expression is given as a binary tree.\n"
  "Each leaf is an integer and each internal node is\n"
  "one of '+', '−', '∗', or '/'.\n"

  "Given the root to such a tree, write a function to evaluate it.\n"

  "For example, given the following tree:\n"

  "    *\n"
  "   / \\n"
  "  +    +\n"
  " / \  / \\n"
  "3  2  4  5\n"
  "You should return 45, as it is (3 + 2) * (4 + 5).\n"
  return output;
}
void printProb(void)
{
  std::cout << prob();
}
