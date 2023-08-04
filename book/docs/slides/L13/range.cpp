#include <iostream>
#include <vector>

std::vector<int> range(int start, int end, int step = 1)
{
    std::vector<int> x;
    for (int i = start; i < end; i += step)
    {
        x.push_back(i);
    }
    return x;
}

std::vector<int> range(int end)
{
    return range(0, end);
}

int main()
{
    auto x = range(5);
    std::cout << "x: ";
    for (auto xi : x)
        std::cout << xi << ", ";

    auto y = range(1, 6, 2);
    std::cout << "\ny: ";
    for (auto yi : y)
        std::cout << yi << ", ";
    std::cout << "\n";

    return 0;
}
