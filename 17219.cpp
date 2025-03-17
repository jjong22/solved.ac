# include <iostream>
# include <map>

using namespace std;

int main()
{
    int n, m;
    string site, password;
    map<string, string> my_site;

    scanf("%d %d", &n, &m);

    for (int i = 0 ; i < n ; i++)
    {
        cin >> site >> password;
        my_site.insert({site, password});
    }

    for (int i = 0; i < m ; i++)
    {
        cin >> site;

        cout << my_site.find(site)->second << '\n';
    }
}