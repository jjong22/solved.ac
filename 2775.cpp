#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int test;
	cin >> test;

	int sum = 0;

	int apart[15][14];

	for (int i = 0; i < 14; i++)
	{
			apart[0][i] = i + 1;
	}

	for (int i = 1; i < 15; i++)
	{
		for (int j = 0; j < 14; j++)
		{
			for (int k = 0; k <= j; k++)
			{
				sum = sum + apart[i - 1][k];
			}
			apart[i][j] = sum;
			sum = 0;
		}
	}
/*
	for (int j = 0; j < 14; j++)
	{
		for (int k = 0; k < 14; k++)
		{
			cout << apart[j][k] << " ";
		}
	}
*/

	vector<int> v1;

	int k, n;
	for (int i = 0; i < test; i++)
	{
		cin >> k;
		cin >> n;

		v1.push_back(k);
		v1.push_back(n);
	}

	for (int i = 0; i < test; i++)
	{
		cout << apart[v1[2*i]][v1[2*i+1]-1] << '\n';
	}
}
