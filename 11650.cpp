# include <iostream>
# include <vector>
# include <algorithm>

int main()
{
    using namespace std;
    vector<vector<int>> v = {};

    int cnt = 0;
    cin >> cnt;
    int a, b;
    
    for (int i ; i < cnt ; i++)
    {   
        cin >> a >> b;
        v.push_back({a, b});
    }

    sort(v.begin(), v.end());

    for(int i ; i < cnt ; i++)
    {
        cout << v[i].front() << " " << v[i].back() << '\n'; 
    }
    
    return 0;
}

// 참고 : https://twinkite.tistory.com/entry/C-2%EC%B0%A8%EC%9B%90-%EB%B2%A1%ED%84%B0-%EC%A0%95%EB%A0%ACsort
