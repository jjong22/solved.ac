# include <iostream>

using namespace std;

int main()
{
    int n, temp;
    int num1, num2;
    int cnt = 1;

    cin >> n;

    temp = n;

    while (1)
    {
        if (n <= 2 * (cnt * 2 - 1) - 1 )
            break;

        n -= 2 * (cnt * 2 - 1) - 1;
        cnt++;
    }

    if (n <= (cnt * 2 - 1))
        num1 = n;
    else
        num1 = 2 * (cnt * 2 - 1) - n ;

    n = temp;
    cnt = 1;

    while (1)
    {
        if (n <= 2 * (cnt * 2) - 1 )
            break;

        n -= 2 * (cnt * 2) - 1;
        cnt++;
    }

    if (n <= (cnt * 2))
        num2 = n;
    else
        num2 = 2 * (cnt * 2) - n;

    
    cout << num1 << "/" << num2 << endl;

    
}