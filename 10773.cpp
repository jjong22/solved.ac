#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int n;
	int sum = 0;
	cin >> n;

	vector<int> eq;

	int num;

	for (int i = 0; i < n; i++)
	{
		cin >> num;
		if (num != 0)
		{
			eq.push_back(num);
		}
		else
		{
			eq.pop_back();
		}
	}

	for (int i = 0; i < eq.size(); i++)
	{
		sum += eq[i];
	}
	cout << sum;
}