#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n, number;
	int sum = 0;
	int total = 0;
	vector<int> v1;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> number;
		v1.push_back(number);
	}

	sort(v1.begin(), v1.end());

	for (int i = 0; i < n; i++)
	{
		sum = sum + (n - i) * v1[i];
	}

	cout << sum;
}