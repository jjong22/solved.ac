#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;
int main()
{
	int r = 31;
	int mod = 1234567891;

	int save_31 = 1;
	int n;
	string word;
	cin >> n;
	cin >> word;

	int sum = 0;

	vector<int> v1;

	for (int i = 0; i < n; i++)
	{
		v1.push_back(word[i] - 96);
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i; j++)
		{
			save_31 = save_31 * 31;
		}
		sum = sum + v1[i] * save_31;
		save_31 = 1;
	}

	sum = sum % mod;

	cout << sum;
}