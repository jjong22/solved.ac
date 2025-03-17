#include <iostream>

int youngmin(int num)
{
    int result = 0;
    num += 1;
    while(num > 0)
    {
        result += 1;
        num -= 30;
    }
    return result * 10;
}

int minsick(int num)
{
    int result = 0;
    num += 1;
    while(num > 0)
    {
        result += 1;
        num -= 60;
    }
    return result * 15;
}


int main()
{
    int n;
    int time;
    int young = 0;
    int min = 0;

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::cin >> time;

        young += youngmin(time);
        min += minsick(time);
    }

    if (young < min)
    {
        std::cout << "Y " << young;
    }
    else if (young == min)
    {
        std::cout << "Y M " << young;
    }
    else 
    {
        std::cout << "M " << min;
    }
}