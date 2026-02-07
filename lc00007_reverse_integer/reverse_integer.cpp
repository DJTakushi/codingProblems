#include <cmath>
#include <vector>
#include "reverse_integer.h"

int Solution::reverse(int x)
{
    std::vector<int> digits;
    int num = x;

    while (num != 0)
    {
        int digit = num % 10;
        digits.push_back(digit);
        num = num / 10;
    }

    double out = 0;
    size_t c = 0;
    for (auto it = digits.rbegin(); it < digits.rend(); ++it)
    {
        out += pow(10, c) * (*it);
        c++;
    }

    double z = pow(2,31);
    if (out > z-1 || out < -1*z){
        out = 0;
    }

    return int(out);
}
