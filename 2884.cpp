#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
    int hour, min;
    cin >> hour >> min;

    if (min < 45 and hour >= 1)
    {
        min += 15;
        hour -= 1;
    }
    else if (min < 45 and hour == 0)
    {
        min += 15;
        hour = 23;
    }
    else
    {
        min -= 45;
    }
    cout << hour << " " << min;
}