#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
int main()
{
	int n, m;
	string name;
	string name1, name2;
	priority_queue<string, vector<string>, greater<string>> qu;
	vector<string> people;

	cin >> n >> m;

	for (int i = 0; i < n+m; i++)
	{
		cin >> name;
		qu.push(name);
	}

	// 이미 사전 순으로 priority_queue에 의해 정렬됨, 옆에 있는 중복된 경우만 세어주면 됨!
	for (int i = 0; i < n + m - 1; i++)
	{
		name1 = qu.top();
		qu.pop();
		name2 = qu.top();

		if (name1 == name2)
		{
			people.push_back(name1);
		}
	}
	

	cout << people.size() << "\n";
	for (int i = 0; i < people.size(); i++)
	{
		cout << people[i] << '\n';
	}
}