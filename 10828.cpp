#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	string input;

	int n, push;
	int number = 0;
	vector<int> q, save;
	vector<string> meong;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> input;
		meong.push_back(input);

		if (input == "push")
		{
			cin >> push;
			save.push_back(push);
		}
	}

	for (int i = 0; i < n; i++)
	{
		if (meong[i] == "push")
		{
			push = save[number];
			q.push_back(push);
			number += 1;
		}
		if (meong[i] == "pop")
		{
			if (q.size() == 0)
			{
				cout << -1 << '\n';
			}
			else
			{
				cout << q[q.size()-1] << '\n';
				q.erase(q.end()-1);
			}
		}
		if (meong[i] == "empty")
		{
			if (q.size() == 0)
			{
				cout << 1 << '\n';
			}
			else
			{
				cout << 0 << '\n';
			}
		}
		if (meong[i] == "size")
		{
			cout << q.size() << '\n';
		}

		if (meong[i] == "top")
		{
			if (q.size() == 0)
			{
				cout << -1 << '\n';
			}
			else
			{
				cout << q[q.size() - 1] << '\n';
			}
		}
	}
}