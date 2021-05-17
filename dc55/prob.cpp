#include <string>
#include <iostream>
#include <vector>
#include "prob.h"
#include "main.h"
std::string prob(void)
{
  std::string output =
  "Daily Coding Problem: Problem #55 [Easy]\n"
  "This problem was asked by Microsoft.\n"
  "Implement a URL shortener with the following methods:\n"
  "  - shorten(url), which shortens the url into a six-character alphanumeric\n"
  "      string, such as zLg6wl.\n"
  "  - restore(short), which expands the shortened string into the original \n"
  "      url. If no such shortened string exists, return null.\n"
  "  Hint: What if we enter the same URL twice?\n\n";
  return output;
}
extern "C" {
  void printProb(void)
  {
    std::cout << prob();
  }
}
