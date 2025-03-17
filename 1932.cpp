#include <iostream>
#include <algorithm>

int arr[500][500];
int dp[500][500];

int main()
{
    int n;
    int max = 0;
    std::cin >> n;

    for (int i = 0; i<n; i++)
        for (int j = 0; j<=i; j++)
            std::cin >> arr[i][j];

    dp[0][0] = arr[0][0];

    for (int i = 1; i<n; i++)
        for (int j = 0; j<=i; j++)
        {
            if (j>0) dp[i][j] = std::max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j];
            else dp[i][j] = dp[i-1][j] + arr[i][j];
        }

    for (int i = 0; i<n; i++)
    {
        if(max < dp[n-1][i]) max = dp[n-1][i];   
    }

    std::cout << max;

    return 0;
}