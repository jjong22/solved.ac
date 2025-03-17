#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int n, x;
	int count = 0;
	
	int memory;

	vector<int> v1, v2;

	cin >> n >> x;

	for (int i = 0; i < n; i++)
	{
		cin >> memory;
		v1.push_back(memory);
	}

	for (int i = 0; i < n; i++)
	{
		if (v1[i] < x)
		{
			v2.push_back(v1[i]);
			count += 1;
		}
	}

	for (int i = 0; i < count; i++)
	{
		cout << v2[i];
		if (i + 1 != count)
		{
			cout << " ";
		}
	}
}