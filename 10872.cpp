#include <cstdlib>
#include <iostream>

int main()
{
    using namespace std;
    
    int n;
    cin >> n;
    
    int sum = 1;
    
    for (int i = 1; i <= n; i++)
    {
        sum = sum * i;
    }
    
    cout << sum;
}