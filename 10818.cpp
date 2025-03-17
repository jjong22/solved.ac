#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int n;
	cin >> n;

	int m;

	vector<int> v1;

	for (int i = 0; i < n; i++)
	{
		cin >> m;
		v1.push_back(m);
	}

	int max, min;
	max = v1[0];
	min = v1[0];

	
	for (int i = 0; i < n; i++)
	{
		if (v1[i] > max)
		{
			max = v1[i];
		}
		else if (v1[i] < min)
		{
			min = v1[i];
		}
	}
	cout << min << " " << max;

}