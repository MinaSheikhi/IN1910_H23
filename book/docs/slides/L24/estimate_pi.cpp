#include <chrono>
#include <cmath>
#include <iostream>

using namespace std::chrono;

extern "C"
{
    double estimate_pi(unsigned int N)
    {
        double pi_fourth = 0.0;
        for (unsigned int i = 0; i < N; i++)
        {
            pi_fourth += std::pow(-1, i) * 1.0 / (2.0 * i + 1.0);
        }
        return 4.0 * pi_fourth;
    }
}

int main()
{
    int N = 1000000;
    int num_repeats = 5;
    int num_runs = 2;
    for (int i = 0; i < num_repeats; i++)
    {
        auto start = high_resolution_clock::now();
        for (int i = 0; i < num_runs; i++)
        {
            estimate_pi(N);
        }
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        std::cout << duration.count() / 1e6 << " ";
    }
    std::cout << "\n";
}
