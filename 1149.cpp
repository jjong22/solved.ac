#include <iostream>
#include <algorithm>

int cost[1000][3];
int now[3];
int pre[3];

int main()
{   
    int n;
    std::cin >> n;

    for (int i = 0; i<n; i++) std::cin >> cost[i][0] >> cost[i][1] >> cost[i][2];

    for (int i = 0; i<n; i++)
    {
        now[0] = std::min(pre[1], pre[2]) + cost[i][0];
        now[1] = std::min(pre[0], pre[2]) + cost[i][1];
        now[2] = std::min(pre[0], pre[1]) + cost[i][2];

        pre[0] = now[0];
        pre[1] = now[1];
        pre[2] = now[2];
    }

    std::cout << std::min(std::min(now[0], now[1]), now[2]);
}