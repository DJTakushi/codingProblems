#include <string>
#include <iostream>
#include <vector>
#include "prob.h"
std::string prob(void)
{
  std::string output =
    "Daily Coding Problem: Problem #47 [Easy]\n"
    "This problem was asked by Facebook.\n\n"

    "Given a array of numbers representing the stock prices of a \n"
    "company in chronological order, write a function that calculates\n"
    "the maximum profit you could have made from buying and selling\n "
    "that stock once. You must buy before you can sell it.\n\n"

    "For example, given [9, 11, 8, 5, 7, 10], you should return 5, \n"
    "since you could buy the stock at 5 dollars and sell it at 10 dollars.\n";
  return output;
}
void printProb(void)
{
  std::cout << prob();
}
