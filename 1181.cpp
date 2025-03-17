# include <iostream>
# include <set>
# include <string>

using namespace std;

struct Compare { // 구조체 재정의를 통한 기준 설정
	bool operator() (const string &a, const string &b) const{
		if (a.size() == b.size())
			return a < b;
		else
			return a.size() < b.size();
	}
};

int main()
{
    ios::sync_with_stdio(0); // 입출력 가속화
	cin.tie(0);

    int n;
    cin >> n;

    set<string, Compare> s;

    string temp;

    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        s.insert(temp);
    }

    for (auto str : s)
    {
        cout << str << '\n';
    }
}