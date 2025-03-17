#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
    int sum[9];
    for (int i = 0; i < 9; i++)
    {
        cin >> sum[i];
    }

    int store = sum[0];
    int place = 1;

    for (int j = 0; j < 9; j++)
    {
        if (sum[j] > store)
        {
            store = sum[j];
            place = j + 1;
        }
    }

    cout << store << '\n';
    cout << place;
}