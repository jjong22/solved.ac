#include <iostream>
#include <cstdlib>

int summation(int n);

using namespace std;
int main()
{
	int n;
	int count = 1;

	cin >> n;

	for (int i = 0; i < n; i++)
	{

		if (n == 1)
		{
			count = 0;
			break;
		}

		if (n > 1 + summation(count - 1) and n <= 1 + summation(count))
		{
			break;
		}

		count = count + 1;
	}

	cout << count + 1;
}

int summation(int n)
{
	int multi = 0;
	for (int i = 1; i <= n; i++)
	{
		multi = multi + i;
	}

	return 6 * multi;
}