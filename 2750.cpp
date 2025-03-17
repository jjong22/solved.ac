# include <iostream>
# include <set>

int main()
{
    using namespace std;

    int n;
    cin >> n;

    set<int> s;

    int num;

    for (int i = 0; i < n; i++)
    {
        cin >> num;
        s.insert(num);
    }

    for (auto iter = s.begin() ; iter != s.end(); iter++)
    {
        cout << *iter << '\n';
    }
}