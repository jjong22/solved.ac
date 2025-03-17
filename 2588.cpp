#include <iostream>
#include <cstdlib>

int main()
{
    int a, b;
    std::cin >> a;
    std::cin >> b;

    int mul1 = b % 10;
    int mul2 = b % 100;
    int mul3 = b - mul2;
    int mul4 = a * b;

    std::cout << a * mul1 << '\n';
    std::cout << a * (mul2-mul1)/10 << '\n';
    std::cout << a * mul3/100 << '\n';
    std::cout << mul4 << '\n';
}