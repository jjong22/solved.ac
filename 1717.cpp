#include <iostream>
#include <algorithm>
int par[1000001];

int root(int i)
{
    if(par[i] == i) return i;
    par[i] = root(par[i]);
    return par[i];
}

void join(int i, int j)
{
    i = root(i); j = root(j);
    if(i == j) return;
    par[j] = i;
}

int main()
{
    int n, m;
    scanf("%d%d", &n, &m);

    for (int i = 1; i <= 1000001; i++)
    {
        par[i] = i;
    }
    for (int i = 0; i < m; i++)
    {
        int oper, a, b;
        scanf("%d%d%d", &oper, &a, &b);

        if (oper == 0)
        {
            join(a, b);
        }
        else
        {
            if (root(a) == root(b)) printf("YES\n");
            // 루트 정점이 같을 경우 같은 집합.
            else printf("NO\n");
        }
    }

    return 0;
}