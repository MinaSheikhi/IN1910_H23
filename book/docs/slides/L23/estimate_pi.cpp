// estimate_pi.cpp
#include <cmath>    // std::pow
#include <iomanip>  // std::setprecision
#include <iostream> // std::cout
#include <string>   // std::stoi

double estimate_pi(unsigned int N)
{
    double pi_fourth = 0.0;
    for (unsigned int i = 0; i < N; i++)
    {
        pi_fourth += std::pow(-1, i) * 1.0 / (2.0 * i + 1.0);
    }
    return 4.0 * pi_fourth;
}

int main(int argc, char **argv)
{

    unsigned N = std::stoi(argv[1]);
    std::cout << std::setprecision(20) << "\u03C0 = " << estimate_pi(N) << "\n";
    return 0;
}
