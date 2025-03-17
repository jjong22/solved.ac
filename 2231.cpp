#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
	int n, result;
	int sum = 0;

	int local;

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		local = i;
		while (local != 0)
		{
			sum = sum + (local % 10);
			local = local / 10;

			if (local < 10)
			{
				sum = sum + local;
				break;
			}
		}

		if (sum + i == n)
		{
			cout << i;
			break;
		}

		sum = 0;
	}

	if (sum == 0)
	{
		cout << sum;
	}
}