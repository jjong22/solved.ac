#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
    int n;

    cin >> n;

    set<int> s_min;

    int num;

    for (int i = 0; i < n; i++)
    {
        cin >> num;
        s_min.insert(num);
    }

    int result = -1;
    int diff = 0;
    
    for (set<int>::iterator iter = s_min.begin(); iter!=s_min.end(); iter++)
    {
        if (next(iter) != s_min.end())
            if(diff < (*next(iter) - *iter) /2)
            {
                diff = (*next(iter) - *iter) / 2;
                result = (*iter + *next(iter)) / 2;
            }
    }

    cout << result;

    
    return 0;
}