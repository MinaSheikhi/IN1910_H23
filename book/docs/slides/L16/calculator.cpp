#include "calculator.hpp"
#include <iostream>

int add(int a, int b)
{
    print("Add");
    return a + b;
}

double divide(int a, int b)
{
    print("Divide");
    return a / ((double)b);
}
