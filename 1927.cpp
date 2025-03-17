#include <iostream>
#include <cstdlib>
#include <queue>
#include <vector>

using namespace std;
int main()
{
	int n;
	cin >> n;

	priority_queue<unsigned int, vector<unsigned int>, greater<unsigned int>> qu;
	unsigned int number;
	vector<unsigned int> v1;

	for (int i = 0; i < n; i++)
	{
		cin >> number;
		v1.push_back(number);
	}

	for (int i = 0; i < n; i++)
	{
		if (v1[i] == 0)
		{
			if (qu.size() == 0)
			{
				cout << 0 << '\n';
			}
			else
			{
				cout << qu.top() << '\n';
				qu.pop();
			}
		}
		else
		{
			qu.push(v1[i]);
		}
	}
}