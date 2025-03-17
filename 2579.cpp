#include <iostream>
#include <algorithm>

int stair[301];
int dp[301];

int cal_dp(int n){
    if (dp[n] != 0) return dp[n];
    else {
        dp[n] = std::max(cal_dp(n-3)+stair[n-1]+stair[n],cal_dp(n-2)+stair[n]);
        return dp[n];
    }
}

int main()
{
    int n;

    std::cin >> n;

    for (int i = 0; i < n; i++) // input
    {
        std::cin >> stair[i];
    }

    dp[0] = stair[0];
    dp[1] = stair[0] + stair[1];
    dp[2] = std::max(stair[0] + stair[2], stair[1] + stair[2]);

    for (int i = 3; i < n; i++)
    {
        cal_dp(i);
    }

    std::cout << dp[n-1] <<'\n';

    return 0;
}