#include <math.h>
#include <stdio.h>

double estimate_pi(unsigned int N)
{
    double pi_fourth = 0.0;
    for (unsigned int i = 0; i < N; i++)
    {
        pi_fourth += pow(-1, i) * 1.0 / (2.0 * i + 1.0);
    }
    return 4.0 * pi_fourth;
}

void print_hello()
{
    printf("Hello world\n");
}

int main()
{
    print_hello();
    return 0;
}
