#include <iostream>
#include <cstdlib>

using namespace std;
int main()
{
	int number[10];
	int comb[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
	int store[10];
	int sum = 0;

	for (int i = 0; i < 10; i++)
	{
		cin >> number[i];
	}

	for (int j = 0; j < 10; j++)
	{
		number[j] = number[j] % 42;
	}

	for (int i = 0; i < 9; i++)
	{
		for (int j = i+1; j < 10; j++)
		{
			if (number[i] == number[j])
			{
				comb[i] = 0;
			}
		}
	}

	for (int i = 0; i < 10; i++)
	{
		sum = sum + comb[i];
	}

	cout << sum;

}