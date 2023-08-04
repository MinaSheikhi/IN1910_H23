#include <fstream>
#include <iostream>
#include <vector>

struct Solution
{
    std::vector<double> t;
    std::vector<double> v;
    std::vector<double> y;
};

Solution falling_body(double v0, double y0, double dt, double T, double g = 9.81)
{
    Solution sol{{0.0}, {v0}, {y0}};

    double t = 0.0;
    int i = 0;
    while (t < T)
    {
        t = i * dt;
        sol.t.push_back(sol.t[i] + dt);
        sol.v.push_back(sol.v[i] - g * dt);
        sol.y.push_back(sol.y[i] + sol.v[i + 1] * dt);
        i++;
    }
    return sol;
}

int main()
{
    // Initial betingelser
    double y0 = 100.0;
    double v0 = 0.0;

    double T = 4.0;
    double dt = 0.01;

    auto solution = falling_body(v0, y0, dt, T);
    std::ofstream ofs{"output.txt"};
    for (int i = 0; i < solution.t.size(); i++)
    {
        std::cout << solution.t[i] << " " << solution.v[i] << " " << solution.y[i] << "\n";
        ofs << solution.t[i] << " " << solution.v[i] << " " << solution.y[i] << "\n";
    }
    ofs.close();
    return 0;
}
