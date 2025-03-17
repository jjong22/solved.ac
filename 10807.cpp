#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int n;
	vector<int> v1;

	cin >> n;

	int number;

	for (int i = 0; i < n; i++)
	{
		cin >> number;
		v1.push_back(number);
	}

	int search;
	int count = 0;

	cin >> search;

	for (int i = 0; i < n; i++)
	{
		if (v1[i] == search)
		{
			count = count + 1;
		}
	}

	cout << count;
}