#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>

using namespace std;
int main()
{
	int n;

	cin >> n;

	int save;
	int sum = 0;
	int count = 0;
	
	vector<int> v1;

	for (int i = 0; i < n; i++)
	{
		cin >> save;
		v1.push_back(save);
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 2; j < 1001; j++)
		{
			if (v1[i] % j == 0)
			{
				count = count + 1;  // 자기 자신일 때만 나누어 떨어지면 소수
			}
		}

		if (count == 1) // 소수 일 때
		{
			sum += 1;
			count = 0;
		}
		else 
		{
			count = 0;
		}
	}

	cout << sum;
}