#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int n, m;
	vector<int> prior;
	bool is_prior = false;

	cin >> n >> m;

	for (int i = n; i <= m; i++)
	{
		is_prior = true;

		for (int j = 2; j*j <= i; j++)
		{
			if (i % j == 0)
			{
				is_prior = false;
				break;
			}
		}

		if (i == 1)
		{
			is_prior = false;
		}

		// 1은 소수가 아닙니다.

		if (is_prior == true)
		{
			prior.push_back(i);
		}
	}

	for (int i = 0; i < prior.size(); i++)
	{
		cout << prior[i] << "\n";
	}
}