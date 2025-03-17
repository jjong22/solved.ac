#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
    int a[5];
    int squr_sum = 0;

    for (int i = 0 ; i < 5; i++)
    {
        cin >> a[i];
    }

    for (int j= 0; j < 5; j++)
    {
        squr_sum = squr_sum + (a[j] * a[j]);
    }
    cout << squr_sum % 10;
}