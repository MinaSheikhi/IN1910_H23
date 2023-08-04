// test_calculator.cpp
#include "calculator.hpp"
#include <cassert>
#include <cmath>
#include <iostream>

const double TOL = 1e-12;

void print(std::string msg)
{
    std::cout << msg << "\n";
}

void test_add()
{
    std::cout << "Test add";
    int a = 3;
    int b = 2;
    int c = add(a, b);
    assert(c == 5);
    std::cout << " - passed\n";
}

void test_divide()
{
    std::cout << "Test divide";
    int a = 3;
    int b = 2;
    double c = divide(a, b);
    double expected = 1.5;
    assert(abs(c - 1.5) < TOL);
    std::cout << " - passed\n";
}

int main()
{
    test_add();
    test_divide();
    return 0;
}
