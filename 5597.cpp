#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	vector<int> v1, v2;

	int n;

	for (int i = 0; i < 28; i++)
	{
		cin >> n;
		v1.push_back(n);
	}

	sort(v1.begin(), v1.end());

	int arr[30] = {0,};

	int jump = 0;

	for (int i = 1; i <= 30; i++)
	{
		if (count(v1.begin(), v1.end(), i))
		{
			0;
		}
		else
		{
			v2.push_back(i);
		}
	}
	
	cout << v2[0] << '\n' << v2[1];
}