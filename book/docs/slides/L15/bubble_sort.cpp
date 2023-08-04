#include <iostream>
#include <vector>

void print(std::vector<int> &input)
{
    for (auto l : input)
    {
        std::cout << l << " ";
    }
    std::cout << "\n";
}

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

void bubble_sort(std::vector<int> &input)
{
    bool swapped;
    for (int end = input.size(); end > 0; end--)
    {
        swapped = false;
        for (int i = 0; i < end - 1; i++)
        {
            if (input[i] > input[i + 1])
            {
                swap(input[i], input[i + 1]);
                swapped = true;
            }
        }
        if (!swapped)
        {
            // No swap was made meaning that the list is sorted
            return;
        }
        print(input);
    }
}

int main()
{

    std::vector<int> lst_sorted{1, 2, 3, 4, 5};
    std::vector<int> lst_sorted_reverse{5, 4, 3, 2, 1};

    std::cout << "\nSorted list:\n";
    bubble_sort(lst_sorted);
    std::cout << "\nReverse sorted list:\n";
    bubble_sort(lst_sorted_reverse);
    return 0;
}
