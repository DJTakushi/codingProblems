#include <cmath>
#include <vector>
#include "my_atoi.h"

int Solution::myAtoi(string s)
{
    double out = 0.0;
    if (s.size() > 0)
    {
        bool numEncountered = false;
        int polarity = 1;
        for (size_t i = 0; i < s.size(); i++)
        {

            switch (s.c_str()[i])
            {
            case ' ':
                if (numEncountered)
                    i = s.size(); // exit
                break;
            case '-':
                if (numEncountered)
                    i = s.size(); // exit
                else
                    polarity = -1;
                numEncountered = true;
                break;
            case '+':
                if (numEncountered)
                    i = s.size(); // exit
                else
                    polarity = 1;
                numEncountered = true;
                break;
            case '0':
            case '1':
            case '2':
            case '3':
            case '4':
            case '5':
            case '6':
            case '7':
            case '8':
            case '9':
                out = out *10.0 + s.c_str()[i] - 48;
                numEncountered = true;
                break;

            default:
                i = s.size(); // exit
            }
        }

        out *= polarity;

        double max = __INT32_MAX__; // pow(2, 31) - 1;
        out = out > max ? max : out;

        double min = pow(2, 31) * -1.0;
        out = out < min ? min : out;
    }

    return int(out);
}
