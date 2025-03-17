#include <iostream>

int T(int num)
{
    return ((num + 1) * num) / 2;
}

int W(int num)
{
    int sum = 0;
    for (int i = 0; i < num; i++)
    {
        sum += (i+1) * T(i + 2);
    }

    return sum;
}

int main()
{
    int n;
    std::cin >> n;

    for(int i = 0; i<n; i++)
    {
        int k;
        std::cin >> k;

        std::cout << W(k) << '\n';
    }
}