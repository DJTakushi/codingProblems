//https://en.cppreference.com/w/cpp/error/assert
#include <iostream>
// uncomment to disable assert()
//#define NDEBUG
#include <cassert>

// Use (void) to silent unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))
#include "hello.h"
int main()
{
    assertm("Hello World!"==HelloWorld(), "HelloWorld() returns incorrect output");
    std::cout << "Pass!";
}
