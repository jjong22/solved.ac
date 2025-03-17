# include <iostream>
# include <map>

using namespace std;

int main()
{
    multimap<int, string> my_map;

    int n, age;
    string name;

    cin >> n;
    for (int i = 0 ; i<n ; i++)
    {   
        cin >> age >> name;
        my_map.insert({age, name});
    }

    for (auto iter : my_map)
    {
        cout << iter.first << " " << iter.second << '\n';
    }
}