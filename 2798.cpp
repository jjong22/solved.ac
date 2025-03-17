#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	int n, m;
	cin >> n >> m;

	int save;
	vector<int> v1;

	int sum;

	for (int i = 0; i <n;i++)
	{
		cin >> save;
		v1.push_back(save);
	}

	sort(v1.begin(), v1.end());

		sum = v1[0] + v1[1] + v1[2];

		int a = 0;
		int b = 1;
		int c = 2;

	for (int i = n - 1; i > 1; i--)
	{
		c = i;
		a = 0;
		b = 1;
		for (int j = 1; j < i; j++)
		{	
			a = 0;
			b = j;
			for (int k = 0; k < j; k++) 
			{
				a = k;

				save = v1[a] + v1[b] + v1[c];
				if (save > sum and save <= m)
				{
					sum = save;
				}
			}
		}
	}

	cout << sum;

}