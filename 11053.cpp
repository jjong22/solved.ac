#include <iostream>
#include <algorithm>

int arr[1000];
int dp[1000];

int main()
{
    int n;

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::cin >> arr[i];
    }   

    dp[0] = 1;

    for (int i = 1; i<n; i++)
    {
        int max = 0;
        for (int j = 0;j < i; j++)
        {
            if (arr[i]>arr[j] && max < dp[j]) max = dp[j];
        }
        dp[i] = max + 1;
    }

    int result = 0;
    for (int i = 0; i<n; i++)
    {
        if (result < dp[i]) result = dp[i];
    }

    std::cout << result;
}