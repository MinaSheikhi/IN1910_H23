#include <iostream>

int main()
{
    int a = 10;
    int &b = a;
    int *c = &a;

    std::cout << "a = " << a << ", b = " << b << ", c = " << c << ", *c = " << *c << "\n";
    std::cout << "Increment a\n";
    a += 5;
    std::cout << "a = " << a << ", b = " << b << ", c = " << c << ", *c = " << *c << "\n";
    std::cout << "Increment b\n";
    b += 5;
    std::cout << "a = " << a << ", b = " << b << ", c = " << c << ", *c = " << *c << "\n";
    std::cout << "Increment c\n";
    *c += 5;
    std::cout << "a = " << a << ", b = " << b << ", c = " << c << ", *c = " << *c << "\n";
    return 0;
}
