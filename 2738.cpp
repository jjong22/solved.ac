#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int a, b;
	cin >> a >> b;

	int arr[100][100] = { 0, };
	int arr2[100][100] = { 0, };
	int arr3[100][100] = {0,};

	int number;

	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			cin >> number;
			arr[i][j] = number;
		}
	}

	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			cin >> number;
			arr2[i][j] = number;
		}
	}

	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			arr3[i][j] = arr[i][j] + arr2[i][j];
			cout << arr3[i][j] << " ";
		}
		cout << '\n';
	}

}