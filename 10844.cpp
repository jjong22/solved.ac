#include <iostream>
#include <algorithm>
using namespace std;

int n;

long dp[105][10];

int main() {
    cin >> n;

    for (int i = 1; i <= 9; i++) dp[1][i] = 1;
    for (int i = 2; i <= n; i++) {
        for (int j = 0; j <=9; j++) {
            if (j ==0) dp[i][j] = dp[i-1][1];
            else if (j == 9) dp[i][j] = dp[i-1][8];
            else dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1];

            dp[i][j] %= 1000000000;
        }
    }

    long answer = 0;
    for (int i = 0; i <=9; i++) answer += dp[n][i];
    cout << answer % 1000000000;
}